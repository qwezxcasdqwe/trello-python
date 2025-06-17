from rest_framework import serializers
from .models import Board,Column,Task,Comment
from django.contrib.auth.models import User

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
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=5) #пароль не возвращаем юзеру
    
    class Meta:
        model = User
        fields = ['username','email','password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        ) 
        return user 