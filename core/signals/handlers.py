from django.db.models.signals import post_save
from core.models import Appointment
from rest_framework.exceptions import ValidationError

from django.dispatch import receiver
from nutrition.utils.send_email_templates import send_accepted_appointment_email, send_cancelled_appointment_email, send_declined_appointment_email
# from nutrition.utils.send_text_message import send_text_message_welcome

from django.db import transaction


@receiver(post_save, sender=Appointment)
def update_user_of_appointment_status(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "confirmed":
            try:
                send_accepted_appointment_email(
                instance.user.email, instance.user.get_full_name())
            except:
                raise ValidationError("Something went Wrong Try again later.")
        elif instance.status == "cancelled":
            send_declined_appointment_email(
                instance.user.email, instance.user.get_full_name())
