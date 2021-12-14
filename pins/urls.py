from django.contrib import admin
from django.urls import path, include

import pins.views as views

urlpatterns = [
    path('pins/', views.ListPins.as_view()),
    path('pin-detail/<int:id>', views.PinDetail.as_view()),
    path('user-boards/', views.UserBoardDetail.as_view()),
    path('user-board-pin/', views.ListAddPinToBoard.as_view()),
]