from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import random
import string
# Create your views here.


def index(request):
    return redirect('main:login')
