from django.contrib import admin
from .models import Appointment, MealPlan, Meal, Health, PatientMealplan, Prescription, Profile


@admin.register(PatientMealplan)
class PatientMealplanAdmin(admin.ModelAdmin):
    list_display = ('get_phone_number', 'get_first_name',
                    'get_last_name', 'get_meal_plan_id')

    def get_phone_number(self, obj):
        return obj.user.phone_number

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_meal_plan_id(self, obj):
        mealplan = obj.meal_plan
        return f"#{mealplan.id} {mealplan.title}"


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


class MealInline(admin.TabularInline):
    model = Meal
    min_num = 0
    max_num = 10
    extra = 2


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = [
        "chef",
        "title",
        "status",
        "created_at",
    ]
    list_per_page = 20
    list_prefe = ["patient", "chef"]
    ordering = ["created_at"]
    search_fields = [
        "user__first_name", "user__last_name", "user__phone_number"
    ]
    list_filter = ['chef', 'status',  'created_at']
    inlines = [MealInline]


admin.site.register(Health)
admin.site.register(Prescription)


@admin.register(Profile)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "image",
    ]
