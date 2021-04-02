from .views import *
from django.urls import path


urlpatterns = [
    path('login', BotLoginAPIView.as_view())
]
