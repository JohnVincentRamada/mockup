from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework import status, authentication, permissions
from .models import Resume, UserDetail, Education, HonorsAwards
from django.contrib.auth.models import User
from . import serializers


class UserSet(APIView):

    def get(self, request, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]

        user = User.objects.filter(id = request.user.id)
        serializer = serializers.UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        
        first_name = serializer.initial_data['first_name']
        last_name = serializer.initial_data['last_name']
        username = serializer.initial_data['username']
        email = serializer.initial_data['email']
        password = serializer.initial_data['password']
        
        if User.objects.filter(username=username):
            return Response({'error': 'Username already exists'})
        if User.objects.filter(email=email):
            return Response({'error': 'Email already exists'})

        if serializer.is_valid():
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()

        return Response(serializer.data)

    def put(self, request):
        user_extract = request.user
        user = User.objects.get(id=user_extract.id)
        serializer = serializers.UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
        return Response(serializer.data)

class ResumeSet(APIView):
    
    def get(self, request, format=None):
        resume = Resume.objects.filter(user = request.user)
        serializer = serializers.ResumeSerializer(resume, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id
        serializer = serializers.ResumeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"error":"not valid data"})
        return Response(serializer.data)
    
    def put(self, request):
        resume = Resume.objects.filter(user=request.user)
        serializer = serializers.ResumeSerializer(resume, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class UserDetailSet(APIView):
    
    def get(self, request, format=None):
        userdetail = UserDetail.objects.filter(user = request.user)
        serializer = serializers.UserDetailSerializer(userdetail, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request):
        user = UserDetail.objects.get(user = request.user)
        serializer = serializers.UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response({"error":"error"})
        return Response(serializer.data)
    
class EducationSet(APIView):

    def get(self, request, format=None):
        education = Education.objects.filter(user = request.user)
        serializer = serializers.EducationSerializer(education, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request):
        education = Education.objects.filter(user=request.user)
        serializer = serializers.EducationSerializer(education, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class HonorsAwardsSet(APIView):

    def get(self, request, format=None):
        honors_awards = HonorsAwards.objects.filter(user = request.user)
        serializer = serializers.HonorsAwardsSerializer(honors_awards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.HonorsAwardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def put(self, request):
        honors_awards = HonorsAwards.objects.filter(user=request.user)
        serializer = serializers.HonorsAwardsSerializer(honors_awards, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    





