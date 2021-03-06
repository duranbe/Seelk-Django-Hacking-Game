from rest_framework import serializers
from .models import TimeAlert, ValueAlert


class TimeAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeAlert
        fields = "__all__"


class ValueAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueAlert
        fields = "__all__"
