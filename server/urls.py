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
    path('yourAccount', account, name="account"),
    path("cp", change_pwd, name="change_pwd"),
    path("t_list", transaction_list, name="transaction_list"),
    path("d_list", delete_transaction_history, name="delete_transactions")

]
