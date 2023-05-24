from rest_framework.serializers import ModelSerializer
from rest_framework import serializers 
from authentication.models import User
from .models import Appointment, Health, Meal, MealPlan, Profile
from authentication.serializers import SimpleUserSerializer

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image"]
                  
class HealthSerialzier(ModelSerializer):
    class Meta:
        model = Health
        fields = ["id","weight","height","blood_type","date_of_birth"]

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
        fields = ["id","type","name","description","created_at"]

    def create(self, validated_data):
        plan_pk = self.context['plan_pk']
        return Meal.objects.create(plan_id=plan_pk, **validated_data)


class MealPlanSerializer(ModelSerializer):
    patient = SimpleUserSerializer(read_only=True)
    chef = SimpleUserSerializer(read_only=True)
    meal_set=MealSerializer(read_only=True,many=True)
    class Meta:
        model = MealPlan
        fields = [
            "id","chef","patient","title","description","status","created_at","meal_set"
        ]
    def create(self, validated_data):
        patient_pk = self.context['patient_pk']
        return MealPlan.objects.create(patient_id=patient_pk, **validated_data)




class PatientSerializer(ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    mealplans=MealPlanSerializer(many=True,read_only=True)
    health=HealthSerialzier(read_only=True)
    class Meta:
        model = User
        fields = ['id', "profile",'first_name', 'last_name',
                  'email','phone_number', "health","mealplans"  ]
        


class BodyMassSerializer(serializers.Serializer):
    height = serializers.FloatField()
    weight = serializers.FloatField()