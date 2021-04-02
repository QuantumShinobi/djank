from rest_framework import generics, status
from rest_framework.response import Response
from server.models import *
from .serializers import *
from rest_framework.views import APIView
# class HeroViewSet(generics.ListAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerailizer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DiscordUserView(APIView):
    serializer_class = BotLoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "User does not exist"})
            else:
                discord = serializer.data.get('discord_username')
                return Response(status=status.HTTP_200_OK, data=UserSerializer(user).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status=status.HTTP_502_BAD_GATEWAY)


# class TestAPIView(APIView):
#     serializer_class = DiscordAccountSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user_id = serializer.data.get('user')
#             user = User.objects.get(id=user_id)
#             return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
