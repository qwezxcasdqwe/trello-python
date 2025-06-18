from rest_framework import serializers

class TelegramAuthSerializer(serializers.Serializer):
    telgram_id = serializers.IntegerField()
    first_name = serializers.CharField()
    username = serializers.CharField()
    
    