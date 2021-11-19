from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.models import Movie
from accounts.models import User


@api_view(['GET', 'POST'])
def get_create_by_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        movie = get_object_or_404(Movie, pk=movie_id)
        revies = movie.review_set.all()
        serializer = ReviewSerializer(revies, many=True)
        return Response(serializer.data)
        

@api_view(['GET'])
def get_by_user(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    revies = person.review_set.all()
    serializer = ReviewSerializer(revies, many=True)
    return Response(serializer.data)