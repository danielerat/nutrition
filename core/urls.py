from django.urls import path, include
from .views import AppointmentViewset, MealplanViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('appointment', AppointmentViewset,
                basename='appointments')
router.register('mealplans', MealplanViewset,
                basename='mealplans')
urlpatterns = [
    path('', include(router.urls)),
]
