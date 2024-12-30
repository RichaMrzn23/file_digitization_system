from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from .permissions import *
# Create your views here.


     

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOnly|IsManagerOnly|IsRegularUserOnly]
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

class Backup_FileView(ModelViewSet):
    queryset = Backup_File.objects.all()
    serializer_class = Backup_FileSerializer

class Recovery_FileView(ModelViewSet):
    queryset = Recovery_File.objects.all()
    serializer_class = Recovery_FileSerializer

class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

# @api_view(['POST'])
# # @permission_classes([AllowAny])
# def register(request ):
    
    # if request.method == 'GET':
    #     serializer = UserSerializer(data=request.data)
    #     if pk is not None:
    #         try:
    #             users= User.objects.get(id=pk)
    #             serializer = UserSerializer(users)
    #             return Response(serializer.data, status = status.HTTP_200_OK)
    #         except User.DoesNotExist:
    #             return Response('User not found', status = status.HTTP_404_NOT_FOUND)
    #     else:
    #         users = User.objects.all()
    #         serializer = UserSerializer( users, many = True)
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    
    # if request.method == 'POST':
        # password = request.data.get('password')
        # hash_password = make_password(password)
        # request.data['password'] = hash_password
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response("User Created", status = status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors)
        
    # if request.method =='DELETE':
    #     serializer = UserSerializer(data=request.data)
    #     if pk is not None:
    #         try:
    #             users = User.objects.get(pk=pk)
    #             users.delete()
    #             return Response("User Deleted!!!", status = status.HTTP_200_OK)

    #         except User.DoesNotExist:
    #             return Response('User not found', status = status.HTTP_404_NOT_FOUND)
            
# from django.http import HttpResponse
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     # return HttpResponse()
#     user = authenticate(username=email, password=password)
#     if user==None:
#         return Response('Email or Password is incorrect!', status=status.HTTP_400_BAD_REQUEST)
#     else:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(token.key, status=status.HTTP_200_OK)


# @permission_classes([AllowAny])
class RegistrationAPIView(APIView):
    def post(self, request):
        # password = request.data.get('password')
        # hash_password = make_password(password)
        # request.data['password'] = hash_password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @permission_classes([AllowAny])
class LoginAPIView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            raise AuthenticationFailed('Missing credentials') # raise error if credentials are not complete
        user = authenticate(request, username = email, password= password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.email, 'role': user.role}, status=status.HTTP_200_OK)
        raise AuthenticationFailed('Invalid credentials')