from django.db import models
from django.conf import settings
MEAL_TYPE_CHOICES = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('snack', 'Snack'),
)
BLOOD_TYPE_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)
STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
)
REVIEW_PROCESS_STATUS = (
    ('pending', 'Pending'),
    ('reviewed', 'Reviewed'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
)


class Appointment(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="appointments", blank=True, null=True,
                               on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Patient Prescription


class Prescription(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='prescriptions')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=15, choices=REVIEW_PROCESS_STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Health(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    blood_type = models.CharField(
        max_length=3, choices=BLOOD_TYPE_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + "'s Health Record@"+self.user.phone_number

# Meal Plan

# Patient Meal Plan


class MealPlan(models.Model):
    chef = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="mealplans",
                             on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=15, choices=REVIEW_PROCESS_STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Patient Meals


class Meal(models.Model):

    plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PatientMealplan(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patient_mealplans")
    meal_plan = models.ForeignKey(
        MealPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name="patient_mealplans")
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'meal_plan')

    def __str__(self):
        return f"{self.user.username}'s Meal Plan"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(default="default.jpg",
                              upload_to="profiles/")
