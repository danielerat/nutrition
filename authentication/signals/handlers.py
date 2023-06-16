from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from core.models import Health, Profile


@receiver(post_save, sender=User)
def create_health_record_and_profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Health.objects.create(user=instance)
        Profile.objects.create(user=instance)
