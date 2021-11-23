from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Genre

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    acc_point = models.IntegerField(default=0)
    curr_point = models.IntegerField(default=0)


class Scoreboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score = models.IntegerField()
    