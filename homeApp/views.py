from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def home(request):
    return render(request, "home.html")


def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are succesfully loggined")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials, Please try again!")
            return redirect("/")

    return HttpResponse("This is login")


def handleSignin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if len(username) < 3 or len(fname) < 3 or len(lname) < 3 or len(email) < 3 or len(pass1):
            messages.error(
                request, "Every field must have atleast 3 char, Please try again!")
            return redirect('/')

        if pass1 != pass2:
            messages.error(
                request, "Password do not match, Please try again!")
            return redirect('/')

        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(
            request, "Your account has been created successfully!")
        return redirect('/')

    return HttpResponse("<h1>404 Not Found</h1>")


def handleLogout(request):
    logout(request)
    messages.success(request, "You are successfully logged out")
    return redirect('/')
