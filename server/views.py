from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.


def index(request):
    try:
        request.COOKIES['user-identity']
    except KeyError:
        return redirect("main:login")
    else:
        id = request.COOKIES['user-identity']
        print(id)
        user = User.objects.get(unique_id=id)

    return render(request, 'main/index.html', context={"user": user})


def login(request):
    try:
        request.COOKIES['user-identity']
    except KeyError:
        return render(request, 'main/login.html')
    else:
        return redirect("main:index")


def singed_up(request):

    if request.method == "POST":
        try:
            request.COOKIES['user-identity']
        except KeyError:
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(username=username).exists() == True:
                return render(request, "main/signup.html", context={'error': "Username has already been taken"})
            else:
                if len(password) < 8:
                    return render(request, "main/signup.html", context={'error': "Password should be atleast 8 characters long"})
                new_user = User.objects.create(
                    username=username, password=password)
                response = render(request, 'main/redirect.html')
                response.set_cookie("user-identity", str(new_user.unique_id))
                return response
        else:
            return redirect("main:index")

    else:
        return HttpResponse("Access Denied")


def signup(request):
    try:
        request.COOKIES['user-identity']
    except KeyError:
        return render(request, 'main/signup.html')
    else:
        return redirect("main:index")


def logged_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists() == True:
            user = User.objects.get(username=username)
            if password == user.password:
                response = render(request, 'main/redirect.html')
                response.set_cookie("user-identity", str(user.unique_id))
                return response
            else:
                return render(request, "main/login.html", context={"error": "Password is incorrect"})
        else:
            return render(request, "main/login.html", context={'error': "There is no account associated with this username"})
    else:
        return HttpResponse("Acces Denied")


def logout(request):
    try:
        request.COOKIES['user-identity']
    except KeyError:
        return redirect("main:index")

    else:
        response = render(request, 'main/logout.html',)
        response.delete_cookie("user-identity")
        return response
