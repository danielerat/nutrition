from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_welcome_email(to, names):
    # Render the email template
    email_template = render_to_string(
        'emails/welcome_email.html', {'names': names})

    # Create an EmailMessage object
    email = EmailMessage(
        'Welcome At Streamlining Device Tracking',  # Subject of the email
        email_template,  # Content of the email (the rendered template)
        settings.DEFAULT_FROM_EMAIL,  # From email address
        [to],  # List of recipient email addresses
    )
    email.content_subtype = 'html'

    # Send the email
    email.send()


def send_accepted_appointment_email(to, names):
    # Render the email template
    email_template = render_to_string(
        'emails/accepted_appointment_email.html', {'names': names})

    # Create an EmailMessage object
    email = EmailMessage(
        'You got yourself an appointment',
        email_template,
        settings.DEFAULT_FROM_EMAIL,
        [to],
    )
    email.content_subtype = 'html'

    # Send the email
    email.send()


def send_declined_appointment_email(to, names):
    # Render the email template
    email_template = render_to_string(
        'emails/declined_appointment_email.html', {'names': names})

    # Create an EmailMessage object
    email = EmailMessage(
        'You do not get yourself an appointment',
        email_template,
        settings.DEFAULT_FROM_EMAIL,
        [to],
    )
    email.content_subtype = 'html'

    # Send the email
    email.send()


def send_cancelled_appointment_email(to, names):
    # Render the email template
    email_template = render_to_string(
        'emails/cancelled_appointment_email.html', {'names': names})

    # Create an EmailMessage object
    email = EmailMessage(
        'You do not get yourself an appointment',
        email_template,
        settings.DEFAULT_FROM_EMAIL,
        [to],
    )
    email.content_subtype = 'html'

    # Send the email
    email.send()
