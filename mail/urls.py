from django.urls import path
from .views import *
app_name = "mail"
urlpatterns = [
    path('', MailView.as_view(), name="index"),
    path('id/<str:id1>/<str:id2>',
         ResetPasswordView.as_view(), name="reset_password_form"),
    path('id', ResetPasswordView.as_view(), name="reset_password"),
    path('verify/<str:id>/', VerifyMail.as_view(), name="verify_mail")

]
