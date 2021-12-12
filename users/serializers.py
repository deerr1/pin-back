from rest_framework import serializers

import users.models as models

class UserForPin(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ['id', 'username','avatar']
