from django.shortcuts import render
from rest_framework import generics
from django.conf import settings
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from random import randint
from rest_framework.views import APIView
from rest_framework.response import Response

import pins.serializers as serializers
import pins.models as models
import datetime


class AddPinToBoard(generics.CreateAPIView):
    serializer_class = serializers.AddPinToBoardSerializer
    # permission_classes = [IsAuthenticated]

class ListPinsOnBoard(generics.ListAPIView):
    serializer_class = serializers.GetPinsOnBoardSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.UserRightBoard.objects.filter(board=self.kwargs.get('id'))
        if len(queryset) == 0:
            raise NotFound()
        queryset = models.BoardPin.objects.filter(board=self.kwargs.get('id'))
        return queryset

class CreatePin(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        pin = data['pin']
        pin['upload_date'] = datetime.datetime.now()
        pin['user'] = request.user
        serializer = serializers.PinsDetailSerializer(data=pin)
        if serializer.is_valid(raise_exception=True):
            board = models.Board.objects.get(id=data['board'])
            pin = models.Pin.objects.create(name=pin['name'], image=pin['image'], description=pin['description'], upload_date=pin['upload_date'], user=pin['user'])
            pinBoard = models.BoardPin.objects.create(pin = pin, board = board)
            pinBoard.save()
        return Response(status=400)

class ListPins(generics.ListAPIView):
    serializer_class = serializers.PinsSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Сделать фильтрацию по интересам пользователя
            queryset = models.Pin.objects.filter(board__access__name = 0).distinct()
        else:
            queryset = models.Pin.objects.filter(board__access__name = 0).distinct()

        return queryset

class CreateUpdateDeleteUserBoard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = serializers.BoadCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            board = models.Board.objects.create(name=data.get('name'), access=data.get('access'))
            rightsBoard = models.UserRightBoard.objects.create(user=request.user, board = board)
            rightsBoard.save()
            return Response(status=201)
        return Response(status=400)

    def put(self):
        pass
    
    def delete(self):
        pass



class ListUserBoards(generics.ListAPIView):
    serializer_class = serializers.UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.UserRightBoard.objects.filter(user = self.request.user.id)
        if (len(queryset) == 0):
            raise NotFound()
        return queryset

class UserBoardDetail(generics.ListAPIView):
    serializer_class = serializers.BoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.Board.objects.filter(id = self.kwargs.get('id'))
        permission = queryset.filter(access__name = 1)
        if len(permission) > 0:
            permission = models.UserRightBoard.objects.filter(board = self.kwargs.get('id'), user=self.request.user.id)
            if len(permission) > 0:
                return queryset
            else:
                raise NotFound()
        else:
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