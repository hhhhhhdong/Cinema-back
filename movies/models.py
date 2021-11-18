from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True) #
    name = models.CharField(max_length=50)

class Movie(models.Model):
    adult = models.BooleanField() #
    backdrop_path = models.CharField(max_length=200) #
    genres = models.ManyToManyField(Genre)
    id = models.IntegerField(primary_key=True) #
    overview = models.TextField(blank=True)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    
