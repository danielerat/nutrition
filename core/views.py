from rest_framework.viewsets import ModelViewSet
from .models import Appointment, Health, Meal,MealPlan
from authentication.models import User
from .serializers import AppointmentSerializer, CreateMealPlanSerializer, CreateMealSerializer, HealthSerialzier,MealPlanSerializer, MealSerializer,PatientSerializer
from rest_framework import  status
from rest_framework.response import Response

class AppointmentViewset(ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class MealPlanViewset(ModelViewSet):
    serializer_class = MealPlanSerializer
    def get_queryset(self):
        return MealPlan.objects.filter()
    def create(self, request, *args, **kwargs):
        serializer = CreateMealPlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MealViewset(ModelViewSet):
    serializer_class = MealSerializer
    def get_queryset(self):
        return Meal.objects.filter(plan_id=self.kwargs['mealplan_pk'])
    def create(self, request, *args, **kwargs):
        plan={"plan_id":kwargs.get("mealplan_pk")}
        serializer = CreateMealSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(**plan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
