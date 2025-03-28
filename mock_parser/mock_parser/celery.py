import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mock_parser.settings")

app = Celery("mock_parser")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update_exchange_rates_every_5_seconds": {
        "task": "mock_parser.tasks.update_exchange_rates",
        "schedule": 5.0,  # Run every 5 seconds
    },
}
