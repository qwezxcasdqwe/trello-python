from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Создает роли и права'
    
    def handle(self,*args, **kwargs):
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        manager_group, _ = Group.objects.get_or_create(name = 'Manager')
        member_group, _ = Group.objects.get_or_create(name='Member')
        
        task_permissions = Permission.objects.filter(content_type__app_label='taskmanager', content_type__model='task')
        
        admin_group.permissions.set(task_permissions)
        manager_group.permissions.set(task_permissions.exclude(codename='delete_task'))
        self.stdout.write(self.style.SUCCESS('Роли успешно созданы'))
        