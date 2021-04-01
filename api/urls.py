from .views import *
from django.urls import path


urlpatterns = [
    path('', UserViewSet.as_view()),
]
