from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from appointment.models import AppointmentApplication
from appointment.serializers import AppointmentSerializer


class AppointmentViewset(ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = AppointmentApplication.objects.all()
