from django.urls import path
from .views import *
app_name = "redirect"
urlpatterns = [
    path('', index, name="index"),

]
