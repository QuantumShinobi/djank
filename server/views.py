import bcrypt
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from .discord import *
from django.shortcuts import redirect, render
from .models import *
from .gen import *

# Create your views here.


def index(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        return render(request, 'main/index.html', context={"user": user})
    else:
        return User.get_user(request=request)


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
    return User.logout(request=request)


def add(request):
    if request.method == "POST":
        money_to_add = request.POST['add_amount']
        id = request.COOKIES['user-identity']
        user = User.objects.get(unique_id=id)
        try:
            user.bank_balance += int(money_to_add)
            user.save()
            new_transaction_created = Transaction(
                user=user, amount=money_to_add, type="add")
            user.transaction(new_transaction_created)
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
            new_transaction_created = Transaction(
                user=user, amount=money_to_withdraw, type="withdraw")
            user.transaction(new_transaction_created)
        return redirect("main:index")
    else:
        return render(request, "error.html", context={"error": "Access Denied"})


def del_account(request):
    if request.method == "POST":
        if isinstance(User.get_user(request=request), User):
            user = User.get_user(request=request)
            user.delete()
            res = render(request, "main/logout.html",
                         context={"text": "Deleting your account"})
            res.delete_cookie("user-identity")
            return res
        else:
            return User.get_user(request=request)
    else:
        return HttpResponse("ACCESS DENIED")


def account(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        return render(request, "main/account.html", context={"user": user})
    else:
        return User.get_user(request)


def change_pwd(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        if request.method == "GET":
            return HttpResponse("Access Denied")
        elif request.method == "POST":
            pwd = request.POST['password']
            hash_pwd = bcrypt.hashpw(
                bytes(pwd, 'utf-8'), bcrypt.gensalt())
            user.password = hash_pwd
            user.save()

            host = request.META['HTTP_HOST']
            return redirect(f"http://{host}/site/yourAccount?pwd_change=true")
    else:
        return User.get_user(request=request)


# Transaction list for user
def transaction_list(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        try:
            transaction_list = user.get_transactions()
        except TypeError:
            return render(request, "main/transactions.html", context={"no_t": "You have no transactions"})
        return render(request, "main/transactions.html", context={"transactions": transaction_list, "host": request.META['HTTP_HOST']})
    else:
        return User.get_user(request=request)


def delete_transaction_history(request):
    if isinstance(User.get_user(request=request), User):
        if request.method == "POST":
            user = User.get_user(request=request)
            user.transaction_list = []
            user.save()
            host = request.META['HTTP_HOST']
            return redirect(f"http://{host}/site/yourAccount?t_list_erase=true")
        else:
            return HttpResponse("Access Denied")


def transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        user = transaction.user
        return render(request, "main/transaction.html", context={"transaction": transaction, "user": user})
    except (Transaction.DoesNotExist, KeyError, ValidationError):
        return HttpResponse("Invalid ID")
