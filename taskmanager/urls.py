from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from boards.views import BoardViewSet, ColumnViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'columns', ColumnViewSet)
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
