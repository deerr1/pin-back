from rest_framework import serializers

import pins.models as models
import users.serializers as user_ser


class PinsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pin
        fields = ['id','image']

class PinsDetailSerializer(serializers.ModelSerializer):
    user = user_ser.UserForPin()
    class Meta:
        model = models.Pin
        fields = ['id', 'name', 'description', 'image', 'upload_date', 'category', 'user']
        depth = 1