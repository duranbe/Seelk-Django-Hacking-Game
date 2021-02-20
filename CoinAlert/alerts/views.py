from django.shortcuts import render
from .serializers import AlertSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Alert
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework import viewsets, status

class AlertViewSet(viewsets.ModelViewSet):
	permissions_classes = [IsAuthenticated]
	serializer_class = AlertSerializer

	def perform_create(self, serializer):
		serializer.save(linked_user=self.request.user)

	def get_queryset(self):
		return Alert.objects.filter(linked_user=self.request.user.id)

