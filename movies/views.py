from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import MovieListSerializer, GenreListSerializer, MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Movie, Genre

# popularity를 기준으로 상위 20개 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def popular(request):
    movies = Movie.objects.order_by('-popularity')[0:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
# vote_average를 기준으로 상위 20개 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def top_rated(request):
    movies = Movie.objects.order_by('-vote_average')[0:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 장르 아이디, 이름을 배열로 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def genre_ids(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

# 장르 아이디를 받아서 해당 장르의 영화리스트 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def genres(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = genre.movie_set.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 영화 디테일 정보 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def loaddata(request):
#     genres = request.data.get('genres')
#     serializer = MovieGenreSerializer(data=genres, many=True)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def loaddata2(request):
#     movies = request.data.get('results')
#     for movie in movies:
#         serializer = MovieSerializer(data=movie)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

