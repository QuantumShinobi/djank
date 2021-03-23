
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import random
import string
# Create your views here.


def index(request):
    return redirect('main:login')


def error_404(request, exception):
    error = "PAGE NOT FOUND"
    return render(request, "error.html", context={"error": error})


def server_error(request, exception=None):
    return render(request, "server_error.html", {})
