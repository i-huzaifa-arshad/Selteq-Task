import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selteq_task.settings")

app = Celery("selteq_task")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
