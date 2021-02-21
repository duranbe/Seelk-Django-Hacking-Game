from django.contrib import admin
from .models import TimeAlert,ValueAlert

# Register your models here.
admin.site.register(TimeAlert)
admin.site.register(ValueAlert)