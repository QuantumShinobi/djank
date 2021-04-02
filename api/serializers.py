from django.db import models
from rest_framework import serializers
from server.models import User, Discord_Account
# from  .models import Hero/

# class HeroSerailizer(serializers.ModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name', 'alias')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bank_balance', 'name', 'unique_id')


class DiscordAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discord_Account
        fields = ("user", 'discord_username',
                  'discord_id', 'bot_key')


class BotLoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    id = models.IntegerField()
    bot_key = serializers.CharField(max_length=200)
    discord_username = serializers.CharField(max_length=37)
