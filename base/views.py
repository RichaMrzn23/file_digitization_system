from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

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

