from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import users.serializers as serializers
import users.models as models

class ListProfile(APIView):
    serializer_class = serializers.UserForProfile
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = models.CustomUser.objects.get(username=kwargs.get('user'))
        if user:
            serializer = serializers.UserForProfile(user)
            data = serializer.data
            if user == request.user:
                data['isYou'] = True
            else:
                data['isYou'] = False
            print(data)
            return Response(data=data)

        return Response(status=404)

class GetUser(APIView):
    serializer_class = serializers.UserForProfile
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = serializers.UserForProfile(request.user)
        return Response(data=serializer.data)
