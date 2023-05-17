from django.db.models.signals import post_save
from appointment.models import AppointmentApplication
from django.dispatch import receiver

from nutrition.utils.send_email_templates import send_accepted_appointment_email
# from nutrition.utils.send_text_message import send_text_message_welcome

from django.db import transaction

from core.models import Appointment


@receiver(post_save, sender=AppointmentApplication)
def update(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "accepted":

            with transaction.atomic():
                send_accepted_appointment_email(
                    instance.user.email, instance.user.get_full_name())
                Appointment.objects.create(
                    user=instance.user,
                    title=instance.title,
                    description=instance.description,
                    start_time=instance.date,
                )

                instance.delete()
