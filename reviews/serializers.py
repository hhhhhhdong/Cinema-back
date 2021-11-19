from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review
from movies.models import Movie, Genre


class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'acc_point',)

    class MovieSerializer(serializers.ModelSerializer):
        class GenreListSerializer(serializers.ModelSerializer):
            class Meta:
                model= Genre
                fields = ('id', 'name',)
        genres = GenreListSerializer(many=True)
        class Meta:
            model = Movie
            fields = ('id', 'poster_path', 'title', 'vote_average', 'release_date', 'genres',)



    user = UserSerializer(read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'content', 'rated', 'like_users', 'user', 'movie',)
