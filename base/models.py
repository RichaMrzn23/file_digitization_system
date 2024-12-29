from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    USER_ROLES=[
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('regular_user', 'Regular_User'),
    
    ]
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

class Backup_File(models.Model):
    BACKUP_TYPES = [
        ('FULL', 'Full Backup'),
        ('INCREMENTAL', 'Incremental Backup'),
        ('DIFFERENTIAL', 'Differential Backup'),
    ]
    
    BACKUP_STATUS = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('IN_PROGRESS', 'In Progress'),
    ]
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='backups')
    backup_file_name = models.CharField(max_length=255)
    backup_file_path = models.FileField(upload_to='backups/') 
    backup_date = models.DateTimeField(auto_now_add=True)
    backup_type = models.CharField(max_length=20, choices=BACKUP_TYPES)
    backup_status = models.CharField(max_length=20, choices=BACKUP_STATUS, default='IN_PROGRESS')
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='backup_performed')
    checksum = models.CharField(max_length=255, null=True, blank=True)

class Recovery_File(models.Model):
    RECOVERY_STATUS = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('PARTIAL', 'Partial Recovery'),
    ]
    
    backup = models.OneToOneField(Backup_File, on_delete=models.CASCADE, related_name='recovery')
    original_file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='recoveries')
    recovery_date = models.DateTimeField(auto_now_add=True)
    recovered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recovery_performed')
    recovery_status = models.CharField(max_length=20, choices=RECOVERY_STATUS)
    recovery_location = models.FileField(upload_to='recovery/') 
    notes = models.TextField(null=True, blank=True)
    
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='feedbacks')
    viewed_date = models.DateField()
    message = models.CharField(max_length=100)
