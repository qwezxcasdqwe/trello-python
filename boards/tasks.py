from celery import shared_task
from django.utils.timezone import now, timedelta
from .models import Task
from django.core.mail import send_mail


@shared_task
def send_deadline_notification():
    upcoming = now() + timedelta(hours=24) # за 24 часа до срока
    tasks = Task.objects.filter(deadline__lte=upcoming, deadline__gte=now, notifed=False)
    
    for task in tasks:
        send_mail(
            subject=f"напоминание о задаче: {task.title}",
            message=f"срок выполнения '{task.title}' приближается: {task.deadline}",
            from_email='no-replu@gmail.com',
            recipient_list=[task.assignee.email]
        )
        
        task.notifed=True
        task.save()
    