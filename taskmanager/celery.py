import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

app = Celery('taskmanager')
app.config_from_object('django.conf:settings', namespace='CELERY') #подгрузка настроек celery
app.autodiscover_tasks() #ищем задачи во всех приложениях

from celery.schedules import crontab

app.conf.beat_schedule = {
    'send-deadline-notification-every-hour': {
        'task': 'boards.tasks.send_deadline-notifications',
        'schedule': crontab(minute=0) #каждый час в 0 минут
    }
}