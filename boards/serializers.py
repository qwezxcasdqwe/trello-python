from rest_framework import serializers
from .models import Board,Column,Task,Comment

class BoardSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Board
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'deadline']
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    fields = ['id', 'task', 'author', 'author_username', 'text', 'created_at']
    read_only_fields = ['author', 'created_at']