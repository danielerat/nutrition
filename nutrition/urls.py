from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('appointments/', include("appointment.urls")),
    path('organization/', include("core.urls")),
]
