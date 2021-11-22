from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Comment
from movies.models import Movie, Genre 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'acc_point',)

class ReviewSerializer(serializers.ModelSerializer):
    

    class MovieSerializer(serializers.ModelSerializer):
        class GenreListSerializer(serializers.ModelSerializer):
            class Meta:
                model= Genre
                fields = ('id', 'name',)
        genres = GenreListSerializer(many=True)
        class Meta:
            model = Movie
            fields = ('id', 'poster_path', 'title', 'vote_average', 'release_date', 'genres', 'backdrop_path', )

    user = UserSerializer(read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'content', 'rated', 'user', 'movie', 'like_users',)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    review = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ('author', 'review', 'content',)