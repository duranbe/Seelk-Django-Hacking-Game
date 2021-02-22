from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import TimeAlert,ValueAlert
from users.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

import requests
import json
from datetime import datetime

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/3')),
    name="time_alert",
    ignore_result=True
)
def time_alert():

	now_base_url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
	before_base_url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}?time={}'
	headers = {'X-CoinAPI-Key' : settings.COINAPI_KEY}

	queryset = TimeAlert.objects.filter(is_activated=True)
	

	if queryset.exists():

		for alert in queryset:

			base_asset = alert.base_asset
			quote_asset = alert.quote_asset
			alert_percent = alert.percentage
			criteria = alert.when_alert

			now_date = datetime.now()
			now_url = now_base_url.format(base_asset,quote_asset)
			now_response = requests.get(now_url, headers=headers)
			now_json_response = json.loads(now_response.text)
			
			
			before_date = now_date - alert.time_delta
			before_url = before_base_url.format(base_asset,quote_asset,before_date.replace(microsecond=0).isoformat())
			before_response = requests.get(before_url, headers=headers)
			before_json_response = json.loads(before_response.text)
			
			now_value = now_json_response['rate']
			before_value = before_json_response['rate']

			if (criteria == 'ABV'):

				augment = 1 + (alert_percent/100)

				if (before_value*augment)==(now_value):

					alert.is_activated = False

					user = alert.linked_user
					user_email = user.email
					subject = f'CoinAlert 🔔 : {base_asset} is above {alert_percent} {quote_asset} !'
					message = f" Hello {user_email},\n {base_asset} is above {alert_percent} {quote_asset} ! Hurry Up ! "
					email_from = settings.EMAIL_HOST_USER
					recipient_list = [user_email]
					send_mail(subject,message, email_from,recipient_list)

					alert.save() 

			if (criteria == 'BLW'):

				decrease = 1 - (alert_percent/100) 

				if (before_value*decrease)==(now_value):

					alert.is_activated = False

					user = alert.linked_user
					user_email = user.email
					subject = f'CoinAlert 🔔 : {base_asset} is below {alert_percent} {quote_asset} !'
					message = f" Hello {user_email},\n {base_asset} is below {alert_percent} {quote_asset} ! Hurry Up ! "
					email_from = settings.EMAIL_HOST_USER
					recipient_list = [user_email]
					send_mail(subject,message, email_from,recipient_list)

					alert.save() 

@periodic_task(
    run_every=(crontab(minute='*/3')),
    name="value_alert",
    ignore_result=True
)
def value_alert():

	base_url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
	headers = {'X-CoinAPI-Key' : settings.COINAPI_KEY}

	queryset = ValueAlert.objects.filter(is_activated=True)

	if queryset.exists():

		for alert in queryset:

			base_asset = alert.base_asset
			quote_asset = alert.quote_asset
			alert_value = alert.coin_value
			criteria = alert.when_alert

			url = base_url.format(base_asset,quote_asset)
			response = requests.get(url, headers=headers)
			json_response = json.loads(response.text)

			api_value = json_response['rate']
			
			if (criteria == 'ABV') and (api_value >= alert_value):

				alert.is_activated = False

				user = alert.linked_user
				user_email = user.email
				subject = f'CoinAlert 🔔 : {base_asset} is above {alert_value} {quote_asset} !'
				message = f" Hello {user_email},\n {base_asset} is above {alert_value} {quote_asset} ! Hurry Up ! "
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user_email]
				send_mail(subject,message, email_from,recipient_list)

				alert.save() 

			if (criteria == 'BLW') and (api_value <= alert_value):

				alert.is_activated = False

				user = alert.linked_user
				user_email = user.email
				subject = f'CoinAlert 🔔 : {base_asset} is below {alert_value} {quote_asset} !'
				message = f" Hello {user_email},\n {base_asset} is below {alert_value} {quote_asset} ! Hurry Up ! "
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user_email]
				send_mail(subject,message, email_from,recipient_list)

				alert.save()