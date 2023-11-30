from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    state_passcode = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    digital_skills = models.TextField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    facebook_handle = models.CharField(max_length=100, blank=True, null=True)
    linkedin_handle = models.CharField(max_length=100, blank=True, null=True)
#  just email & phone number
    def __str__(self):
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in weeks or months


    def __str__(self):
        return self.title
    

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # Progress in percentage

    def __str__(self):
        return self.progress
    


admission_status = (

    ('pending', "pending"),
    ('approved', "approved")
)

class Admission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=admission_status, default='pending', max_length=200)

    def __str__(self):
        return self.date_applied
    


class InternApply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_choices = [
        ('office', 'Office'),
        ('remote', 'Remote'),
    ]
    location = models.CharField(max_length=10, choices=location_choices)

    def __str__(self):
        return self.location
    


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    


class Collaborator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_image = models.ImageField(upload_to='task')
    progress = models.IntegerField(default=0)  # In percentage

    def __str__(self):
        return self.description
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile')
    # Other info ?

    def __str__(self):
        return self.user

