from django.urls import path, include
from .views import AppointmentViewset, BodyMassAPIView, ConversationViewset, HealthViewset,\
    MealPlanViewset, MealViewset, MessageViewSet, PatientViewset, PrescriptionViewset

from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('appointment', AppointmentViewset,
                basename='appointments')
router.register('me', PatientViewset,
                basename='patients')

me_router = routers.NestedSimpleRouter(
    router, 'me', lookup='patient')
me_router.register('health', HealthViewset, basename='patient-health')
me_router.register('mealplan', MealPlanViewset, basename='patient-mealplan')
me_router.register('prescription', PrescriptionViewset,
                   basename='patient-prescription')
me_router.register('conversation', ConversationViewset,
                   basename='conversation')

meal_router = routers.NestedSimpleRouter(
    me_router, 'mealplan', lookup='mealplan')
meal_router.register('meal', MealViewset, basename='meal')

conversation_router = routers.NestedSimpleRouter(
    me_router, 'conversation', lookup='conversation'
)
conversation_router.register(
    'messages', MessageViewSet, basename='conversation-messages'
)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(me_router.urls)),
    path('', include(meal_router.urls)),
    path('', include(conversation_router.urls)),
    path('body-mass/', BodyMassAPIView.as_view(), name='body_mass'),
]
