from django.shortcuts import render


def home(request):
    return render(request=request, template_name="home.html")


def login(request):
    return render(request=request, template_name="login.html")


def register(request):
    return render(request=request, template_name="register.html")
