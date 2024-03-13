import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-every-5-minutes': {
        'task': 'gym.tasks.beat_func',
        'schedule': crontab(minute='*/5'),
    },
}

#celery -A core beat -l info
#celery -A core worker -l info
#sudo service redis-server start (stop)