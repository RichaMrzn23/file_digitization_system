from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

USER_ROLES=[
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('regular_user', 'Regular_User')
]
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='username')
    role = models.CharField(max_length=50, choices= USER_ROLES, default='regular_user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()
    
class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='user_profile')
    position = models.CharField(max_length=50)
    image = models.ImageField(null= True)

class File(models.Model): 
    department = models.ForeignKey(Department, on_delete = models.CASCADE, related_name='files')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    size = models.IntegerField()
    file_uploaded_date = models.DateField(auto_now_add=True)
    file_uploaded_by = models.ForeignKey(User_Profile, on_delete= models.CASCADE, null=True)
    file_path = models.FileField(upload_to='files/')

class Metadata(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE, related_name='metedata')
    keywords = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    creation_date = models.DateField()
    last_modified_date = models.DateField()


ACTION_CHOICES = [
    ('upload', 'Upload'),
    ('edit', 'Edit'),
    ('delete', 'Delete'),
    ('access', 'Access'),
]
class Audit_Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audit_logs')
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    action = models.CharField(max_length= 50, choices= ACTION_CHOICES)
    timestamp = models.DateField()
    details = models.CharField(max_length=100)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='feedbacks')
    viewed_date = models.DateField()
    message = models.CharField(max_length=100)
