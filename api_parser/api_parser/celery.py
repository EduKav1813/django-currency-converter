import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_parser.settings")

app = Celery("api_parser")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update_exchange_rates_every_30_seconds": {
        "task": "api_parser.tasks.update_exchange_rates",
        "schedule": 30,  # Run every 30 seconds
    },
}
