from django.db import models
from django.contrib.auth.models import User

class TelegramProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} ({self.telegram_id})"
