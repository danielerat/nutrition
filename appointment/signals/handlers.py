from django.db.models.signals import post_save
from appointment.models import AppointmentApplication
from rest_framework.exceptions import ValidationError

from django.dispatch import receiver
from rest_framework.views import exception_handler
from nutrition.utils.send_email_templates import send_accepted_appointment_email, send_cancelled_appointment_email, send_declined_appointment_email
# from nutrition.utils.send_text_message import send_text_message_welcome

from django.db import transaction

from core.models import Appointment


@receiver(post_save, sender=AppointmentApplication)
def update(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "accepted":
            try:
                with transaction.atomic():
                    Appointment.objects.create(
                        user=instance.user,
                        title=instance.title,
                        description=instance.description,
                        start_time=instance.date,
                    )
                    instance.delete()
                    send_accepted_appointment_email(
                        instance.user.email, instance.user.get_full_name())
            except:
                raise ValidationError("Something went Wrong Try again later.")
        elif instance.status == "declined":
            send_declined_appointment_email(
                instance.user.email, instance.user.get_full_name())
            instance.delete()
        elif instance.status == "cancelled":
            send_cancelled_appointment_email(
                instance.user.email, instance.user.get_full_name())
            instance.delete()
