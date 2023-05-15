from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from uuid import uuid4


DEVICE_CATEGORY_CHOICES = (
    ("phone", "Phone"),
    ("computer", "Computer"),
    ("tablet", "Tablet"),
    ("accessory", "Accessory"),
    ("others", "Others"),
)
STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)
# Patient profile


# Patient Appointment Application
# User Requests for an application.


class AppointmentApplication():

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
