from django.db import models
from django.conf import settings
from uuid import uuid4
CHRONIC_DISEASE_CHOICES = (
    ('diabetes', 'Diabetes'),
    ('hypertension', 'Hypertension'),
    ('allergies', 'Allergies'),
    ('other', 'Other'),
    ('none', 'None'),
)

ACTIVITY_LEVEL_CHOICES = (
    ('sedentary', 'Sedentary'),
    ('moderate', 'Moderate'),
    ('active', 'Active'),
)

SMOKING_HABIT_CHOICES = (
    ('never', 'Never'),
    ('occasional', 'Occasional'),
    ('regular', 'Regular'),
)

ALCOHOL_CONSUMPTION_CHOICES = (
    ('never', 'Never'),
    ('occasional', 'Occasional'),
    ('regular', 'Regular'),
)

SLEEP_PATTERNS_CHOICES = (
    ('less_than_6_hours', 'Less than 6 hours'),
    ('6_to_8_hours', '6 to 8 hours'),
    ('more_than_8_hours', 'More than 8 hours'),
)

CURRENT_DIET_CHOICES = (
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
    ('omnivorous', 'Omnivorous'),
)

FOOD_ALLERGY_CHOICES = (
    ('gluten', 'Gluten'),
    ('dairy', 'Dairy'),
    ('nuts', 'Nuts'),
    ('other', 'Other'),
    ('none', 'None'),
)


class Conversation(models.Model):

    id = models.UUIDField(primary_key=True, editable=False,
                          unique=True, default=uuid4)
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_conversations', null=True, blank=True
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation between {self.doctor} and {self.patient}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message by {self.sender} in {self.conversation}"


class Questionnaire(models.Model):
    conversation = models.OneToOneField(
        Conversation, on_delete=models.CASCADE, null=True, blank=True)
    chronic_diseases = models.CharField(
        max_length=100, choices=CHRONIC_DISEASE_CHOICES)
    activity_level = models.CharField(
        max_length=20, choices=ACTIVITY_LEVEL_CHOICES)
    smoking_habits = models.CharField(
        max_length=20, choices=SMOKING_HABIT_CHOICES)
    alcohol_consumption = models.CharField(
        max_length=20, choices=ALCOHOL_CONSUMPTION_CHOICES)
    sleep_patterns = models.CharField(
        max_length=20, choices=SLEEP_PATTERNS_CHOICES)
    current_diet = models.CharField(
        max_length=20, choices=CURRENT_DIET_CHOICES)
    food_allergies = models.CharField(
        max_length=100, choices=FOOD_ALLERGY_CHOICES)
    physical_disability = models.BooleanField(default=False)

    def __str__(self):
        return f"Questionnaire for {self.conversation}"
