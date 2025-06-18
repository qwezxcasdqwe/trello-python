from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import TelegramProfile
from .serializers import TelegramAuthSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class TelegramAuthView(APIView):
    def post(self, request):
        serializer = TelegramAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        tg_id = data['telegram_id']
        user_profile = TelegramProfile.objects.filter(telegram_id=tg_id).first()

        if user_profile:
            user = user_profile.user
        else:
            user = User.objects.create(username=f"tg_{tg_id}")
            TelegramProfile.objects.create(
                user=user,
                telegram_id=tg_id,
                first_name=data['first_name'],
                username=data.get('username', '')
            )

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })