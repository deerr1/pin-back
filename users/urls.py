from django.contrib import admin
from django.urls import path, include

import users.views as views

urlpatterns = [
    path('user/', views.GetUser.as_view()),
    path('user-profile/<str:user>', views.ListProfile.as_view()),
]