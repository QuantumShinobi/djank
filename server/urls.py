from django.urls import path
from .views import *
app_name = "main"
urlpatterns = [
    path('index', index, name="index"),
    path('login', login, name="login"),
    path('signed_up', signed_up, name="signed_up"),
    path('logged_in', logged_in, name="logged_in"),
    path('signup', signup, name="signup"),
    path('logout', logout, name="logout"),
    path('a', add, name="add"),
    path('w', withdraw, name="withdraw"),
    path('del', del_account, name="delete_account"),

]
