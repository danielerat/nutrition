from django.db import models
from django.conf import settings


STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'accepted'),
    ('declined', 'declined'),
    ('cancelled', 'cancelled'),
)
# Patient profile


# Patient Appointment Application
# User Requests for an application.


class AppointmentApplication(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
