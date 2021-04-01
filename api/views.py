from rest_framework import generics
from server.models import User, Discord_Account
from .serializers import UserSerializer
# Create your views here.


# class HeroViewSet(generics.ListAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerailizer
class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
