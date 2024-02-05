from django.db import models
from django.conf import settings

# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    address = models.CharField(max_length=100)
    contact_number = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    linkedin_link = models.CharField(max_length=100)
    summary = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    
class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    image = models.ImageField(upload_to='school/')
    year_started = models.IntegerField()
    year_ended = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

class HonorsAwards(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    award = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    image = models.ImageField(upload_to='honors/')
    issued = models.DateField()
    description = models.CharField(max_length=255)

    created_at = models.DateField(auto_now_add=True)