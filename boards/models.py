from django.db import models
from django.contrib.auth.models import User 

class Board(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
      return self.tittle

class Column(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='columns')
    
    class Meta:
         ordering = ['order']  #сортировка по order
    
    def __str__(self):
        return f"{self.board.title} - {self.title}"  # Пример: "Проект X - To Do"     
         
class Task(models.Model):
    PRIORITY_CHOICES= [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title