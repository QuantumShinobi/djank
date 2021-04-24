from django.db import models
from rest_framework import serializers
from server.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bank_balance', 'name', 'unique_id')


class BotLoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    id = models.IntegerField()
    bot_key = serializers.CharField(max_length=200)
    discord_username = serializers.CharField(max_length=37)

    # # TODO: Make Other Bot APIs
