from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
# Create your views here.

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class User_ProfileView(ModelViewSet):
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer


class FileView(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer  


class MetadataView(ModelViewSet):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer   

class Auto_LogView(ModelViewSet):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer

class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

@api_view(['GET','POST','DELETE'])
@permission_classes([AllowAny])
def register(request, pk=None):

    if request.method == 'GET':
        serializers = UserSerializer(data=request.data)
        if pk is not None:
            try:
                users= User.objects.get(id=pk)
                serializer = UserSerializer(users)
                return Response(serializer.data, status = status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response('User not found', status = status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer( users, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response("User Created", status = status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors)
        
    if request.method =='DELETE':
        if pk is not None:
            try:
                users = User.objects.get(pk=pk)
                users.delete()
                return Response("User Deleted!!!")

            except User.DoesNotExist:
                return Response('User not found', status = status.HTTP_404_NOT_FOUND)
            

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user==None:
        return Response('Email or Password is incorrect!', status=status.HTTP_400_BAD_REQUEST)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token.key, status=status.HTTP_200_OK)

