# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from .serializers import MovieGenreSerializer, MovieSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from .models import Movie, Genre

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
