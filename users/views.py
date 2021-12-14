from django.shortcuts import render
from rest_framework import generics

import users.serializers as serializers
import users.models as models

class ListProfile(generics.ListAPIView):
    serializer_class = serializers.UserForProfile

    def get_queryset(self):
        queryset = models.CustomUser.objects.filter(id=self.request.user.id)
        return queryset