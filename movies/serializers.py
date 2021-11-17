from rest_framework import serializers
from .models import Genre, Movie

class MovieGenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('genres', )

