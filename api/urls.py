from .views import *
from django.urls import path


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login")
]
