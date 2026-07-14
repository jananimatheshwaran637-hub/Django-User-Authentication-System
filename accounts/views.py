from django.shortcuts import render, redirect
from .models import User


def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            User.objects.get(
                username=username,
                password=password
            )
            return redirect("register")

        except User.DoesNotExist:
            message = "Invalid Username or Password"

    return render(request, "login.html", {"message": message})


def register_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        User.objects.create(
            username=username,
            password=password
        )

        message = "Registration Successful"

    return render(request, "register.html", {"message": message})