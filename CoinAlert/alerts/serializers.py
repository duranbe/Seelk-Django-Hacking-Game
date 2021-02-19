from rest_framework import serializers


class AlertSerializer(serializers.ModelSerializer):
	class Meta:
        model = Snippet
        fields = '__all__'