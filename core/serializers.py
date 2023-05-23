from os import read
from rest_framework.serializers import ModelSerializer

from authentication.models import User
from .models import Appointment, Health, Meal, MealPlan, Profile
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


class CreateMealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ["plan","type","name","description"]


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id","type","name","description","created_at"]




class PatientSerializer(ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    mealplans=MealPlanSerializer(many=True,read_only=True)
    health=HealthSerialzier(read_only=True)
    class Meta:
        model = User
        fields = ['id', "profile",'first_name', 'last_name',
                  'email','phone_number', "health","mealplans"  ]