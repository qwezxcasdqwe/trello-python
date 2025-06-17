from django.shortcuts import render
from rest_framework import viewsets
from .models import Board,Column,Task,Comment
from .serializers import BoardSerializer, ColumnSerializer, TaskSerializer,CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsManager, IsMember

class BoardViewSet(viewsets.ModelViewSet):
  queryset = Board.objects.all()
  serializer_class = BoardSerializer

class ColumnViewSet(viewsets.ModelViewSet):
  queryset = Column.objects.all()
  serializer_class = ColumnSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsAuthenticated()]
        elif self.request.method in ['POST']:
            return [IsAdmin() | IsManager()]
        elif self.request.method in ['PUT', 'PATCH']:
            return [IsAdmin() | IsManager()]
        elif self.request.method == 'DELETE':
            return [IsAdmin()]
        return super().get_permissions()

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  
  def perform_create(self, serializer):
     serializer.save(author=self.request.user) #подставновка текущего автора при создании комментария

    


