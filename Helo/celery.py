from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helo.settings')

broker = 'redis://127.0.0.1:6379/0'
backend = 'redis://127.0.0.1:6379/0'

app = Celery('Helo', broker=broker, backend=backend)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def add(x, y):
    return x + y