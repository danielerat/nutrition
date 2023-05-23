from django.urls import path, include
from .views import AppointmentViewset, HealthViewset, MealPlanViewset, MealViewset, PatientViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('appointment', AppointmentViewset,
                basename='appointments')
router.register('me', PatientViewset,
                basename='patients')

me_router = routers.NestedSimpleRouter(
    router, 'me', lookup='patient')
me_router.register('health', HealthViewset, basename='patient-health')
me_router.register('mealplan', MealPlanViewset, basename='patient-mealplan',)

meal_router = routers.NestedSimpleRouter(me_router, 'mealplan', lookup='mealplan')
meal_router.register('meal', MealViewset, basename='meal')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(me_router.urls)),
    path('', include(meal_router.urls)),
]
