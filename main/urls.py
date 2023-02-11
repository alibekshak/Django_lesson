from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("contact/", views.contact),
    path("about", views.about),
    path('portfolio', views.portfolio),
    path("signin_signup", views.signin_signup),

]