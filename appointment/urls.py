from django.urls import path, include
from appointment.views import AppointmentViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('appoointment', AppointmentViewset,
                basename='appointments')
urlpatterns = [
    path('', include(router.urls)),
]
