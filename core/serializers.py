from rest_framework.serializers import ModelSerializer
from .models import Appointment, Meal, MealPlan
from authentication.serializers import SimpleUserSerializer


class AppointmentSerializer(ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    doctor = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "user",
            "title",
            "description",
            "start_time",
            "end_time",
            "status",
            "created_at",
            "updated_at"
        ]

class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ["type","name","description","created_at"]

class MealPlanSerializer(ModelSerializer):
    patient = SimpleUserSerializer(read_only=True)
    chef = SimpleUserSerializer(read_only=True)
    meal_set=MealSerializer(read_only=True,many=True)
    class Meta:
        model = MealPlan
        fields = [
            "id","chef","patient","title","description","status","created_at","meal_set"
        ]
