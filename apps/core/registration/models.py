from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        'Avatar', upload_to='profiles', null=True, blank=True)
    biografia = models.TextField('Biografía', blank=True, null=True)
