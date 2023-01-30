import os
import logging 
from celery import Celery
from celery.schedules import crontab

logger = logging.getLogger('celery')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tt_web_app.settings')

celery_app = Celery('app')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

def task():
    logger.info('Task')


celery_app.conf.beat_schedule = {
    'change-polls-state-to-process': {
        'task': 'tt_web_app.celery.task',
        'schedule': crontab(minute='*'),
    }
}
