from os import read
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User
from chat.serializers import SimpleConversationSerializer
from .models import Appointment, Health, Meal, MealPlan, PatientMealplan, Prescription, Profile
from authentication.serializers import SimpleUserSerializer


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image"]


class HealthSerialzier(ModelSerializer):
    class Meta:
        model = Health
        fields = ["id", "weight", "height", "blood_type", "date_of_birth"]


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


class PrescriptionSerializer(ModelSerializer):
    class Meta:
        model = Prescription
        fields = ["id", "doctor", "patient", "title",
                  "description", "status", "created_at"]


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "type", "name", "description", "created_at"]

    def create(self, validated_data):
        plan_pk = self.context['plan_pk']
        return Meal.objects.create(plan_id=plan_pk, **validated_data)


class MealPlanSerializer(ModelSerializer):
    chef = SimpleUserSerializer(read_only=True)
    meal_set = MealSerializer(read_only=True, many=True)

    class Meta:
        model = MealPlan
        fields = [
            "id", "chef", "title", "description", "status", "created_at", "meal_set"
        ]

    def create(self, validated_data):
        return MealPlan.objects.create(**validated_data)


class PatientSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    health = HealthSerialzier(read_only=True)
    patient_mealplans = serializers.SerializerMethodField(read_only=True)
    prescriptions = PrescriptionSerializer(many=True, read_only=True)
    patient_conversations = SimpleConversationSerializer(
        many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', "profile", 'first_name', 'last_name',
                  'email', 'phone_number', 'account_type', "health", "patient_mealplans", "prescriptions", "patient_conversations"]

    def get_patient_mealplans(self, obj):
        patient_mealplans = PatientMealplan.objects.filter(user=obj)
        mealplans = [mealplan.meal_plan for mealplan in patient_mealplans]
        serializer = MealPlanSerializer(mealplans, many=True, read_only=True)
        return serializer.data


class BodyMassSerializer(serializers.Serializer):
    height = serializers.FloatField()
    weight = serializers.FloatField()
