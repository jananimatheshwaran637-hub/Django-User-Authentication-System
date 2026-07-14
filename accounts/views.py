from django.shortcuts import render
from .models import User


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
            message = "Invalid Username or Password"


    return render(
        request,
        "login.html",
        {
            "message": message
        }
    )