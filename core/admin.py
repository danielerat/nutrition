from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "start_time",
        "end_time",
        "status",
        "created_at"
    ]
    list_per_page = 20
    list_select_related = ["user"]
    ordering = ["created_at"]
    search_fields = [
        "user__first_name", "user__last_name", "user__phone_number"
    ]
    list_filter = ['status',  'created_at']
