import bcrypt
from django.http.response import HttpResponse
from .discord import *
from django.shortcuts import redirect, render
from .models import *
from .gen import *
import re
# Create your views here.


def index(request):
    try:
        request.COOKIES['user-identity']
    except (KeyError):
        return redirect("main:login")
    else:
        id = request.COOKIES['user-identity']
        try:
            user = User.objects.get(unique_id=id)
        except User.DoesNotExist:
            res = render(request, "main/logout.html",
                         context={"text": "Loading"})
            res.delete_cookie("user-identity")
            return res

    return render(request, 'main/index.html', context={"user": user})


def login(request):
    try:
        request.COOKIES['user-identity']
    except KeyError:
        return render(request, 'main/login.html')
    else:
        return redirect("main:index")


def signed_up(request):

    if request.method == "POST":
        try:
            request.COOKIES['user-identity']
        except KeyError:
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name']
            discord_username = request.POST['discord_username']
            if User.objects.filter(username=username).exists() == True:
                return render(request, "main/signup.html", context={'error': "Username has already been taken"})
            else:
                if len(password) < 8:
                    return render(request, "main/signup.html", context={'error': "Password should be atleast 8 characters long"})
                hash_pwd = bcrypt.hashpw(
                    bytes(password, 'utf-8'), bcrypt.gensalt())
                name = name.capitalize()
                new_user = User.objects.create(

                    username=username, password=hash_pwd, name=name)
                response = render(request, 'main/logout.html',
                                  context={"title": "Sign up", "text": "Creating your account"})
                response.set_cookie("user-identity", str(new_user.unique_id))
                # and re.search(r"\w", discord_username) and format_is_correct(username):
                if discord_username != "":
                    check = format_is_correct(discord_username)
                    if check == None or check == "Blank Username":
                        # note = "Your discord account was not connected either because the field was blank or because the format was not correct"
                        response.set_cookie(
                            "discord_account", "None")
                    else:
                        response.set_cookie(
                            "discord_account", "True")

                    new_discord_ac = Discord_Account.objects.create(
                        user=new_user, discord_username=discord_username)
                    # response.set_cookie("discord_account", "yes")
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
            return user.authenticate(password, request)
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
        response = render(request, 'main/logout.html',
                          context={"title": "Logout", "text": "Logging you out"})
        response.delete_cookie("user-identity")
        return response


def add(request):
    if request.method == "POST":
        money_to_add = request.POST['add_amount']
        id = request.COOKIES['user-identity']
        user = User.objects.get(unique_id=id)
        try:
            user.bank_balance += int(money_to_add)
            user.save()
        except ValueError:
            return render(request, "error.html", context={"error": "How can u add a non-number field to your bank balance ?"})
        return redirect("main:index")
    else:
        return render(request, "error.html", context={"error": "Access Denied"})


def withdraw(request):
    if request.method == "POST":
        money_to_withdraw = request.POST['withdraw_amount']
        id = request.COOKIES['user-identity']
        user = User.objects.get(unique_id=id)
        try:
            money_to_withdraw = int(money_to_withdraw)
        except ValueError:
            return render(request, "error.html", context={"error": "How can u withdraw a non-number field to your bank balance ?"})

        if int(money_to_withdraw) > user.bank_balance:
            return render(request, "error.html", context={"error": "How can your withdraw amount be greater than your bank balance"})
        else:
            user.bank_balance -= int(money_to_withdraw)
            user.save()
        return redirect("main:index")
    else:
        return render(request, "error.html", context={"error": "Access Denied"})


def del_account(request):
    try:
        request.COOKIES['user-identity']
    except (KeyError):
        return redirect("main:login")
    else:
        id = request.COOKIES['user-identity']
        try:
            user = User.objects.get(unique_id=id)
        except User.DoesNotExist:
            res = render(request, "main/logout.html",
                         context={"text": "Loading"})
            res.delete_cookie("user-identity")
            return res
        else:
            user.delete()
            res = render(request, "main/logout.html",
                         context={"text": "Deleting your account"})
            return res
