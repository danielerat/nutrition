from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from core.utils.HEALTH_CALCULATOR import HEALTH_CALCULATOR
from .models import Appointment, Health, Meal, MealPlan, Prescription
from authentication.models import User
from .serializers import AppointmentSerializer, BodyMassSerializer, HealthSerialzier, MealPlanSerializer, MealSerializer, PatientSerializer, PrescriptionSerializer
from rest_framework import status
from rest_framework.response import Response


class AppointmentViewset(ModelViewSet):
    permission_classes = []
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class PrescriptionViewset(ModelViewSet):
    permission_classes = []
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()


# Patient Serializer
class PatientViewset(ModelViewSet):
    permission_classes = []
    serializer_class = PatientSerializer
    queryset = User.objects.all()


class HealthViewset(ModelViewSet):
    serializer_class = HealthSerialzier

    def get_queryset(self):
        return Health.objects.filter(user_id=self.kwargs['patient_pk'])

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Creation of Health instances is not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class MealPlanViewset(ModelViewSet):
    serializer_class = MealPlanSerializer

    def get_queryset(self):
        patient_id = self.kwargs.get("patient_pk")
        return MealPlan.objects.filter(patient_mealplans__user_id=patient_id)

    def get_serializer_context(self):
        return {"patient_pk": self.kwargs.get("patient_pk")}


class MealViewset(ModelViewSet):
    serializer_class = MealSerializer

    def get_queryset(self):
        return Meal.objects.filter(plan_id=self.kwargs['mealplan_pk'])

    def get_serializer_context(self):
        return {"plan_pk": self.kwargs.get("mealplan_pk")}


class BodyMassAPIView(APIView):
    def post(self, request):
        serializer = BodyMassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        height = serializer.validated_data['height']
        weight = serializer.validated_data['weight']
        body_mass = HEALTH_CALCULATOR.calculate_bmi(height, weight)
        response_data = HEALTH_CALCULATOR.parse_bmi(body_mass)
        return Response(response_data, status=status.HTTP_200_OK)
