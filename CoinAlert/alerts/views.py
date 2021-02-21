from django.shortcuts import render
from .serializers import TimeAlertSerializer,ValueAlertSerializer
from rest_framework.permissions import IsAuthenticated
from .models import TimeAlert,ValueAlert
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework import viewsets, status

class TimeAlertViewSet(viewsets.ModelViewSet):
	permissions_classes = [IsAuthenticated]
	serializer_class = TimeAlertSerializer

	def perform_create(self, serializer):
		serializer.save(linked_user=self.request.user)

	def get_queryset(self):
		return TimeAlert.objects.filter(linked_user=self.request.user.id)

class ValueAlertViewSet(viewsets.ModelViewSet):
	permissions_classes = [IsAuthenticated]
	serializer_class = ValueAlertSerializer

	def perform_create(self, serializer):
		serializer.save(linked_user=self.request.user)

	def get_queryset(self):
		return ValueAlert.objects.filter(linked_user=self.request.user.id)

