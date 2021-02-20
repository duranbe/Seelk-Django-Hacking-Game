from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import Alert
from users.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

import requests
import json

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/3')),
    name="get_coin_price",
    ignore_result=True
)
def get_coin_price():

	base_url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
	headers = {'X-CoinAPI-Key' : settings.COINAPI_KEY}

	queryset = Alert.objects.filter(is_activated=True)

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
			
			if criteria == 'ABV':

				if api_value >= alert_value:
					
					alert.is_activated = False

					user = alert.linked_user
					user_email = user.email
					subject = f'CoinAlert 🔔 : {base_asset} is above {alert_value} {quote_asset} !'
					message = f" Hello {user_email},\n {base_asset} is above {alert_value} {quote_asset} ! Hurry Up ! "
					email_from = settings.EMAIL_HOST_USER
					recipient_list = [user_email]
					send_mail(subject,message, email_from,recipient_list)

					alert.save() 

			if criteria == 'BLW':

				if api_value <= alert_value:

					alert.is_activated = False

					user = alert.linked_user
					user_email = user.email
					subject = f'CoinAlert 🔔 : {base_asset} is below {alert_value} {quote_asset} !'
					message = f" Hello {user_email},\n {base_asset} is below {alert_value} {quote_asset} ! Hurry Up ! "
					email_from = settings.EMAIL_HOST_USER
					recipient_list = [user_email]
					send_mail(subject,message, email_from,recipient_list)

					alert.save() 