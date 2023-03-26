from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilePic(models.Model):
    user = models.OneToOneField(User, related_name="Profile_Pic", on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profilePics', blank=True)

    def __str__(self):
        return self.user.username
