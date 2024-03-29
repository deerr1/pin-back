from django.contrib import admin
from django.urls import path, include

import pins.views as views

urlpatterns = [
    path('pins/', views.ListPins.as_view()),
    path('pin-detail/', views.PinDetail.as_view()),
    path('pin-detail/<int:id>', views.PinDetail.as_view()),
    path('pin-detail/<int:board>/<int:id>/', views.PinDetail.as_view()),
    path('pin-create/', views.CreatePin.as_view()),
    path('user-changed-board/', views.CreateUpdateDeleteUserBoard.as_view()),
    path('user-changed-board/<int:id>', views.CreateUpdateDeleteUserBoard.as_view()),
    path('user-boards/<str:user>', views.ListUserBoards.as_view()),
    path('user-board-detail/<int:id>', views.UserBoardDetail2.as_view()),
    path('user-add-pin-on-board/', views.AddPinToBoard.as_view()),
    path('pins-on-board/<int:id>', views.ListPinsOnBoard.as_view()),
]