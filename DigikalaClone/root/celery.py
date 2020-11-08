
from celery import Celery
from celery.schedules import crontab
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

celery_app = Celery('root')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

# add periodic task for django celery-beat
celery_app.conf.beat_schedule = {
    'update-digikala': {
        'task': 'WebMarketManagementApp.digikala.tasks.update_products',
        'schedule': crontab(minute='*',hour='*/3'),
        
    },
}
