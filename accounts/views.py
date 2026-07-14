from django.shortcuts import render, redirect
from .models import User


def register_view(request):

    message = ""

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        User.objects.create(
            username=username,
            email="",
            password=password
        )

        message = "Registration Successful"


    return render(
        request,
        "register.html",
        {
            "message": message
        }
    )



def login_view(request):

    message = ""

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = User.objects.filter(
            username=username,
            password=password
        ).first()


        if user:
            message = "Login Successful"
        else:
            message = "Invalid Username and Password"


    return render(
        request,
        "login.html",
        {
            "message": message
        }
    )