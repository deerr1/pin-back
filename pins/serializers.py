from rest_framework import serializers

import pins.models as models
import users.serializers as user_ser

class BoadCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Board
        fields = ['name', 'access']

class BoardSerializer(serializers.ModelSerializer):
    img = serializers.FileField(source='random_pin')
    class Meta:
        model = models.Board
        fields = ['id', 'name', 'access', 'img']

class UserBoardSerializer(serializers.ModelSerializer):
    board = BoardSerializer()
    class Meta:
        model = models.UserRightBoard
        fields = ['user', 'board']

class PinsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pin
        fields = ['id','name','image']

class PinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pin
        fields = ['id', 'name', 'description', 'image', 'upload_date', 'user']
        depth = 1
class PinsDetailSerializer(serializers.ModelSerializer):
    user = user_ser.UserForPin()
    class Meta:
        model = models.Pin
        fields = ['id', 'name', 'description', 'image', 'upload_date', 'user']
        depth = 1
class GetPinsOnBoardSerializer(serializers.ModelSerializer):
    pin = PinsSerializer()
    class Meta:
        model = models.BoardPin
        fields = ['board','pin']

class AddPinToBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BoardPin
        fields = ['pin', 'board']