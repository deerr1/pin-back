from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser

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
            if data['avatar'] != None:
                data['avatar'] = 'http://'+request.get_host()+data['avatar']
            print(data)
            return Response(data=data)

        return Response(status=404)


class ChangeProfile(APIView):
    serializer_class = serializers.UserForProfile
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, *args, **kwargs):
        data = request.data
        print(data)
        user = models.CustomUser.objects.get(id = request.user.id)
        if data.get('avatar') and data['avatar']:
            print(data['avatar'])
            user.avatar = data['avatar']
        
        if data.get('username') and data.get('email'):
            user_name = models.CustomUser.objects.filter(username = data['username'])
            user_email = models.CustomUser.objects.filter(username = data['email'])
            print(len(user_email.filter(id=request.user.id)) == 0)
            if (len(user_name)>0 and len(user_name.filter(id=request.user.id))==0) or (len(user_email)>0 and len(user_email.filter(id=request.user.id))==0):
                return Response(status=400)
            else:
                user = models.CustomUser.objects.get(id = request.user.id)
                user.username = data['username']
                user.email = data['email']


        user.save()
        return Response(status=200)


class GetUser(APIView):
    serializer_class = serializers.UserForProfile
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = serializers.UserForProfile(request.user)
        print(serializer.data)
        data = serializer.data.copy()
        if data['avatar'] != None:
            data['avatar'] = 'http://'+request.get_host()+data['avatar']
        return Response(data=data)
