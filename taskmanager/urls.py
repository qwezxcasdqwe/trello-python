from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from boards.views import BoardViewSet, ColumnViewSet, TaskViewSet
from ..boards.views import CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import TelegramAuthView

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'columns', ColumnViewSet)
router.register(r'task', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh', TokenObtainPairView.as_view(), name='token_refresh'),
    path('api/accounts/',include('accounts.urls')),
    path('telegram-auth/', TelegramAuthView.as_view(), name='telegram-auth'),
]
