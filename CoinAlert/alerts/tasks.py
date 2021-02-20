from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import Alert
from CoinAlert import settings

logger = get_task_logger(__name__)

import requests
import json

@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="get_coin_price",
    ignore_result=True
)
def get_coin_price():

	base_url = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
	headers = {'X-CoinAPI-Key' : settings.COINAPI_KEY}

	queryset = Alert.objects.filter(is_activated=True)

	if queryset.exists():

		for alert in queryset:

			url = base_url.format(alert.base_asset,alert.quote_asset)
			response = requests.get(url, headers=headers)
			json_response = json.loads(response.text)


			api_value = json_response['rate']
			alert_value = alert.coin_value
			criteria = alert.when_alert

			if criteria == 'ABV':

				if api_value >= alert_value:
					
					alert.is_activated = False
					alert.save() 

			if criteria == 'BLW':

				if api_value <= alert_value:

					alert.is_activated = False
					alert.save() 


			f = open("test_log.txt", "a")
			f.write(response.text)
			f.write(f'{api_value} - {criteria} - {alert_value}')
			f.close()