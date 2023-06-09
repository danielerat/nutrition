from django.urls import path, include
from appointment.views import AppointmentViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('applications', AppointmentViewset,
                basename='applications')
urlpatterns = [
    path('', include(router.urls)),
]
