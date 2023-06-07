# Generated by Django 4.2.1 on 2023-05-23 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='chef',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mealplans', to=settings.AUTH_USER_MODEL),
        ),
    ]