from django.shortcuts import render
from rest_framework import generics
from django.conf import settings
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

import pins.serializers as serializers
import pins.models as models


class ListAddPinToBoard(generics.ListCreateAPIView):
    queryset = models.BoardPin.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.GetPinsOnBoardSerializer
        elif self.request.method == 'POST':
            return serializers.AddPinToBoardSerializer

    # def post(self):


class ListPins(generics.ListAPIView):
    serializer_class = serializers.PinsSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Сделать фильтрацию по интересам пользователя
            queryset = models.Pin.objects.filter(board__access__name = 0).distinct()
        else:
            queryset = models.Pin.objects.filter(board__access__name = 0).distinct()

        return queryset

class UserBoardDetail(generics.ListAPIView):
    serializer_class = serializers.UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = models.UserRightBoard.objects.filter(user = self.request.user.id)
            if (len(queryset) == 0):
                raise NotFound()
            return queryset

class PinDetail(generics.ListAPIView):
    serializer_class = serializers.PinsDetailSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = models.Pin.objects.filter(id = self.kwargs.get('id'))
            filtered_queryset = queryset.filter(board__access__name = 1, board__user_righs_board = self.request.user.id)
            if len(filtered_queryset) == 1:
                queryset = filtered_queryset
            else:
                queryset = queryset.filter(board__access__name = 0)
        else:
            queryset = models.Pin.objects.filter(id = self.kwargs.get('id'), board__access__name = 0)
        if len(queryset) == 0:
            raise NotFound()
        return queryset