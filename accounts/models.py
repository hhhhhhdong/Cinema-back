from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    acc_point = models.IntegerField(default=0)
    curr_point = models.IntegerField(default=0)