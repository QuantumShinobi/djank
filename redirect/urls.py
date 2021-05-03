from django.urls import path
from .views import *
app_name = "redirect"
urlpatterns = [
    path('', index, name="index"),
    path('link', link, name="create_link"),
    path('redirect/<str:id>/', redirect_pg, name="redirect"),
    path('cs', create_link, name="cs"),
    path('r/<str:id>/', redirect_link, name="redirect_link")

]
