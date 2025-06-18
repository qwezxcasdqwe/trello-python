from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task, TaskHistory
from threading import local


_user = local()

def set_current_user(user):
    _user.value = user

def get_current_user():
    return getattr(_user,'value',None)

@receiver(post_save,sender=Task)
def log_task_save(sender, instance, created, **kwargs): 
    user = get_current_user()
    action = 'crated' if created else 'updated'
    TaskHistory.objects.create(
        task=instance,
        user=user,
        action=action,
        description=f"задача была {action} пользователем {user}" if user else f"Задача была {action}"
    )   