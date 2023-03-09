from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("Brasil", views.Brasil, name="brasil"),
     path("Argentina", views.Argentina, name="argentina"),
     path("Bolivia", views.Bolivia, name="bolivia")
 ]