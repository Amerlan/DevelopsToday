import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

celery_app = Celery("conf")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "reset-upvote": {
        "task": "posts.tasks.reset_upvote",
        "schedule": crontab(hour=0, minute=0),
    },
}
