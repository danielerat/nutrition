from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
from django.contrib.auth.models import AbstractUser

from authentication.user_manager import CustomUserManager

CHOICES_ACCOUNT_TYPE = (
    ("n", "Nutritionist"),
    ("c", "Chef"),
    ("p", "Patient"),
)

# Custom User Model that is Only Unique to this project.


class User(AbstractUser):

    # remove the username field
    username = None

    # add the phone_number field as the new unique identifier
    phone_number = models.CharField(
        validators=[RegexValidator(
            r'^07\d{8}$', "Phone number must be exactly 10 digits and must be a rwandan Number.")],
        max_length=10,
        unique=True,
        null=False,
        blank=False,
        help_text="Phone number must be exactly 10 digits and start with '07'"
    )
    email = models.EmailField(unique=True, null=False,
                              blank=False)

    # Accound type for users
    account_type = models.CharField(
        choices=CHOICES_ACCOUNT_TYPE, default="p", max_length=2, null=True
    )

    # set the phone_number field as the USERNAME_FIELD
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    # set the CustomUserManager as the default manager
    objects = CustomUserManager()
