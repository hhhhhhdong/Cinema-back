from django.db import models
from django.conf import settings

from movies.models import Movie

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    reated = models.IntegerField()
