from rest_framework import status
from .serializers import MovieGenreSerializer, MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def loaddata(request):
    genres = request.data.get('genres')

    serializer = MovieGenreSerializer(data=genres, many=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def loaddata2(request):
    movies = request.data.get('results')

    serializer = MovieSerializer(data=movies, many=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

