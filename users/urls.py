from django.contrib import admin
from django.urls import path, include

import users.views as views

urlpatterns = [
    path('user-profile/', views.ListProfile.as_view()),
]