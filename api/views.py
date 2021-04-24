from rest_framework import status
from rest_framework.response import Response
from server.models import *
from .serializers import *
from rest_framework.views import APIView
from bank.settings import SECRET_KEY


class BotLoginAPIView(APIView):
    serializer_class = BotLoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            bot_key = serializer.data.get('bot_key')
            if bot_key == SECRET_KEY:
                username = serializer.data.get('username')
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "User does not exist"})
                else:
                    pwd = serializer.data.get('password')
                    if user.authenticate(pwd, request, bot=True):
                        discord = serializer.data.get('discord_username')
                        try:
                            discord_ac = Discord_Account.objects.get(
                                discord_username=discord, user=user)
                        except Discord_Account.DoesNotExist:
                            return Response(data={"error": "This discord account has not been linked"}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            d_user = discord_ac.user
                            if d_user.unique_id == user.unique_id:
                                discord_ac.is_verified = True
                                discord_ac.save()
                            else:
                                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={"error": "Your discord account in the site and request dont match"})

                    return Response(status=status.HTTP_200_OK, data=UserSerializer(user).data)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN, data={"error": "Request  Source is not verified"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={"error": "GET request is not allowed"})


class AmountAPIView(APIView):
    serializer_class = 


#
#
#
#
#
#
#
#
#
# ?  PREVIOUS API VIEWS WHICH ARE NO LONGER NEEDED
# class UserView(generics.ListAPIView):
    #     queryset = User.objects.all()
    #     serializer_class = UserSerializer

# class TestAPIView(APIView):
#     serializer_class = DiscordAccountSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user_id = serializer.data.get('user')
    #             user = User.objects.get(id=user_id)
    #             return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
