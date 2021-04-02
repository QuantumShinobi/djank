from .views import *
from django.urls import path


urlpatterns = [
    path('', UserViewSet.as_view()),
    path('post', TestAPIView.as_view()),
    path('discord', DiscordUserView.as_view())
]
