from django.urls import path, include
from .views import AppointmentViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('appointment', AppointmentViewset,
                basename='appointments')
urlpatterns = [
    path('', include(router.urls)),
]
