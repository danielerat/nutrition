from rest_framework.viewsets import ModelViewSet
from .models import Appointment,MealPlan
from .serializers import AppointmentSerializer,MealPlanSerializer


class AppointmentViewset(ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class MealplanViewset(ModelViewSet):
    permission_classes = []
    serializer_class = MealPlanSerializer
    queryset = MealPlan.objects.all()