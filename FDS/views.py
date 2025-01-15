from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *  
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status




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

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   

class FileView(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class Audit_LogView(ModelViewSet):
    queryset = Audit_Log.objects.all()
    serializer_class = Audit_LogSerializer

class Access_RequestView(ModelViewSet):
    queryset = Access_Request.objects.all()
    serializer_class = Access_RequestSerializer

class File_BackupView(ModelViewSet):
    queryset = File_Backup.objects.all()
    serializer_class = File_BackupSerializer

class File_RecoveryView(ModelViewSet):
    queryset = File_Recovery.objects.all()
    serializer_class = File_RecoverySerializer

# class WorkflowView(ModelViewSet):
#     queryset = Workflow.objects.all()
#     serializer_class = WorkflowSerializer

# class Worlflow_ResponsibilityView(ModelViewSet):
#     queryset = Workflow_Responsibility.objects.all()
#     serializer_class = Workflow_ResponsibilitySerializer

class Notification_TokenView(ModelViewSet):
    queryset = Notification_Token.objects.all()
    serializer_class = Notification_TokenSerializer

class NotificationView(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer   

class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if  email ==None or password == None:
            raise AuthenticationFailed('Missing credentials')
        
        user = authenticate(username=email, password=password)
        print(user)
        if user != None:
            token, create = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username' : user.email, 'role': user.role}, status=status.HTTP_200_OK)
        raise AuthenticationFailed('Invalid credentials')
    
    
# class LogoutAPIView(APIView):
#     def post(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)