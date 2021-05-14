from django.urls import path
from .views import *
app_name = "discord"
urlpatterns = [
    path('', LoginView.as_view(), name="verify")

]
