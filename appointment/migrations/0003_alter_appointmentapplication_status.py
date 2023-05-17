# Generated by Django 4.2.1 on 2023-05-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointmentapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentapplication',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'accepted'), ('declined', 'declined'), ('cancelled', 'cancelled')], default='pending', max_length=20),
        ),
    ]
