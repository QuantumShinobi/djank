from django.urls import path
from .views import *
app_name = "main"
urlpatterns = [
    path('index', index, name="index"),
    path('login', login, name="login"),
    path('singed_up', singed_up, name="singed_up"),
    path('logged_in', logged_in, name="logged_in"),
    path('signup', signup, name="signup"),
    path('logout', logout, name="logout")

]
