
FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE nutrition.settings

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
