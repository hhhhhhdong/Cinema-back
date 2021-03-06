from rest_framework import serializers
from .models import Genre, Movie


class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model= Genre
            fields = ('id', 'name',)
            
class MovieListSerializer(serializers.ModelSerializer):
    
    genres = GenreListSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average', 'genres', 'poster_path', 'backdrop_path',)

class MovieSerializer(serializers.ModelSerializer):
    
    genres = GenreListSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


# class GenreListIdSerializer(serializers.ModelSerializer):
#         class Meta:
#             model= Genre
#             fields = ('id',)





# class MovieGenreSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Genre
#         fields = '__all__'

# class MovieSerializer(serializers.ModelSerializer):
#     genre_ids = serializers.ListField(write_only=True)

#     def create(self, validated_data):
#         genre_ids = validated_data.pop('genre_ids')
#         movie = Movie.objects.create(**validated_data)
#         for genre_pk in genre_ids:
#             movie.genres.add(genre_pk)
#         return movie
        
#     class Meta:
#         model = Movie
#         exclude = ('genres', )