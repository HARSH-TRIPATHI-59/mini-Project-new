from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()


class Contact(models.Model):
    user = models.CharField(max_length=200)
    email = models.TextField(blank=True)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.user



class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="videos/%y")
    def __str__(self):
        return self.caption
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Dealer(models.Model):
    user = models.CharField(max_length=200)
    email = models.TextField(blank=True)
    ph_number = models.IntegerField()
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.user
