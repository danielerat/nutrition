from django.contrib import admin
from appointment.models import AppointmentApplication


@admin.register(AppointmentApplication)
class AppointmentApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "date",
        "status",
        "created_at"
    ]
    list_per_page = 20
    list_select_related = ["user"]
    ordering = ["date", "created_at"]
    search_fields = [
        "user__first_name", "user__last_name", "user__phone_number"
    ]
    list_filter = ['status', 'date', 'created_at']
