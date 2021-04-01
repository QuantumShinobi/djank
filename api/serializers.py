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
