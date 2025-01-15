from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_ROLES=[
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('standard_user', 'Standard_User'),
    ('viewer', 'Viewer')
    
    ]
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='username')
    role = models.CharField(max_length=50, choices= USER_ROLES  , default='standard_user')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Department(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user_images/")

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class File(models.Model):
    FILE_TYPE=[
         ('PDF', 'PDF'),
        ('WORD', 'Word Document'),
        ('IMAGE', 'Image'),
        ('AUDIO', 'Audio'),
        ('VIDEO', 'Video'),
        ('SPREADSHEET', 'Spreadsheet'),
        ('PRESENTATION', 'Presentation'),
        ('ZIP', 'Compressed File'),
        ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('REQUEST_CHANGES', 'Request Changes'),
    ]
    file = models.FileField(upload_to="files/")
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=FILE_TYPE)
    size = models.CharField(max_length=15)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING') 
    file_uploaded_date = models.DateTimeField(auto_now_add=True)
    file_uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_files")
    accessible_user = models.ManyToManyField(User, related_name="accessible_files")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Audit_Log(models.Model):
    ACTION_CHOICES = [
    ('upload', 'Upload'),
    ('edit', 'Edit'),
    ('delete', 'Delete'),
    ('access', 'Access'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audit_logs')
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    modified_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return  {self.file.name} + {self.action}

class Access_Request(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="access_requests")
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='access_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    reason = models.TextField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reviewed_requests")
    reviewed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Access Request for {self.file.name}"

class File_Backup(models.Model):
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
    backup_file_name = models.CharField(max_length=100)
    backup_file = models.FileField(upload_to="backups/")
    backup_status = models.CharField(max_length=20, choices=BACKUP_STATUS, default='IN_PROGRESS')
    backup_type = models.CharField(max_length=20, choices=BACKUP_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    backuped_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='backup_performed')

    def __str__(self):
        return self.backup_file_name

class File_Recovery(models.Model):
    RECOVERY_STATUS = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('PARTIAL', 'Partial Recovery'),
    ]
    recovery_file = models.OneToOneField(File_Backup, on_delete=models.CASCADE, null=True, blank= True,related_name='recovery')
    recovered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="recovery_performed")
    recovery_status = models.CharField(max_length=20, choices=RECOVERY_STATUS, default='PARTIAL')
    created_at = models.DateTimeField(auto_now_add=True)
    recovery_location = models.FileField(upload_to="recovery/")

    def __str__(self):
        return f"File Recovery for {self.recovery_file.backup_file_name}"

# class Workflow(models.Model):
#     WORKFLOW_STATUS = [
#         ('PENDING', 'Pending'),
#         ('APPROVED', 'Approved'),
#         ('REJECTED', 'Rejected'),
#     ]
#     file = models.ForeignKey(File, on_delete=models.CASCADE)
#     initiated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="initiated_workflows")
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_workflows")
#     status = models.CharField(max_length=20 , choices=WORKFLOW_STATUS, default='PENDING')
#     comments = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Workflow for {self.file.name}"

# class Workflow_Responsibility(models.Model):
#     workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
#     description = models.TextField()

#     def __str__(self):
#         return self.description

class Notification_Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=150, unique=True)
    device_type = models.CharField(max_length=50, choices=[('android', 'Android'), ('ios', 'iOS'),('web','WEB')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return {self.user.username} + {self.token}


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('TASK_ASSIGNED', 'Task Assigned'),
        ('TASK_UPDATED', 'Task Updated'),
        ('WORKFLOW_STATUS', 'Workflow Status Change'),
        ('SYSTEM_ALERT', 'System Alert'),
        ('FILE_UPLOADED', 'File Uploaded'),
        ('ACCESS_CHANGED', 'Access Changed'),
        ('BACKUP_COMPLETED', 'Backup Completed'),
        ('RECOVERY_COMPLETED', 'Recovery Completed'),
        ('DEADLINE_REMINDER', 'Deadline Reminder'),
    ]
    title = models.CharField(max_length=150)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    notification_token = models.ForeignKey(Notification_Token, on_delete=models.CASCADE, related_name='notifications')
    related_file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='feedbacks')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
