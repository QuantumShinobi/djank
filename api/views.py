from rest_framework import generics, status
from rest_framework.response import Response
from server.models import User, Discord_Account
from .serializers import *
from rest_framework.views import APIView
# class HeroViewSet(generics.ListAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerailizer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestAPIView(APIView):
    serializer_class = DiscordAccountSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_id = serializer.data.get('user')
            user = User.objects.get(id=user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
