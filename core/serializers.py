
from rest_framework.serializers import ModelSerializer
from .models import Appointment
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
