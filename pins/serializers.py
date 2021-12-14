from rest_framework import serializers

import pins.models as models
import users.serializers as user_ser


class BoardSerialuzer(serializers.ModelSerializer):

    class Meta:
        model = models.Board
        fields = ['id', 'name', 'access']

class UserBoardSerializer(serializers.ModelSerializer):
    board = BoardSerialuzer()
    class Meta:
        model = models.UserRightBoard
        fields = ['user', 'board']

class PinsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pin
        fields = ['id','name','image']

class PinsDetailSerializer(serializers.ModelSerializer):
    user = user_ser.UserForPin()
    class Meta:
        model = models.Pin
        fields = ['id', 'name', 'description', 'image', 'upload_date', 'category', 'user']
        depth = 1

class GetPinsOnBoardSerializer(serializers.ModelSerializer):
    pin = PinsDetailSerializer()
    class Meta:
        model = models.BoardPin
        fields = ['pin',]

class AddPinToBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardPin
        fields = ['pin', 'board']