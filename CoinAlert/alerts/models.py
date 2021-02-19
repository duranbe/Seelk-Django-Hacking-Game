from django.db import models

class Alert(models.Model):
    title = models.CharField(max_length=255)
    base_asset = models.CharField(max_length=3) # 3 Alphanumeric Char, see ISO 4217 currency codes
    quote_asset = models.CharField(max_length=3)  # 3 Alphanumeric Char, see ISO 4217 currency codes
    alert_choices = [
		('ABV','Above'),
		('BLW','Below'),
	]
    when_alert = models.CharField(max_length=3,choices=alert_choices,default='Above')
    coin_value	= models.DecimalField(max_digits=25,decimal_places=15)
    is_activated = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)
    linked_user = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE)
