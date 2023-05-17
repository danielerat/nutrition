from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewset(ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
