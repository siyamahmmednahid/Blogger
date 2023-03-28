from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileInfo(models.Model):
    user = models.OneToOneField(User, related_name="ProfilePic", on_delete=models.CASCADE)
    profilePic = models.ImageField(upload_to='profilePics', blank=True, unique=True)
    coverPic = models.ImageField(upload_to='coverPics', blank=True, unique=True)
    shortIntro = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    about = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)


    def __str__(self):
        return self.user.username
