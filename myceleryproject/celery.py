import os
from celery import Celery
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myceleryproject.settings')

app = Celery('myceleryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.  
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task
def add(x,y):
     return x+y

# # Method 2
# app.conf.beat_schedule = {
#      'every-10-seconds'   : {
#         'task':'app.tasks.clear_session_cache',
#         'schedule':timedelta(seconds=10),
#         'args':('11111',)
#     }
# }


# Method 2
# Advance Level Task Scheduling
app.conf.beat_schedule = {
     'every-10-seconds'   : {
        'task':'app.tasks.clear_session_cache',
        'schedule':crontab(minute='*/1'), # every 1 minute
        'args':('11111',)
    }
}