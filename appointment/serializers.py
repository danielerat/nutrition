
from rest_framework.serializers import ModelSerializer
from appointment.models import AppointmentApplication


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = AppointmentApplication
        fields = [
            "user",
            "user",
            "title",
            "description",
            "date",
            "status",
            "created_at"]
