from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def contact(request):
    return  render(request, "main/contact.html")


def about(requsets):
    return render(requsets, "main/about.html")


def portfolio(requsets):
    return render(requsets, "main/portfolio.html")


def signin_signup(requsets):
    return render(requsets, "main/signin_signup.html")