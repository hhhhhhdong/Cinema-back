from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ReviewSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.models import Movie
from accounts.models import User
from .models import Comment, Review


@api_view(['GET', 'POST'])
def get_create_by_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        # 같은 영화에 리뷰를 쓰는 것을 방지
        if movie.review_set.filter(user_id=request.user.pk).exists():
            return Response({'detail': '이미 작성 하셨습니다.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            # 이 영화의 리뷰에 전에 같은 점수(rated)를 준 유저의 포인트를 올려야한다.
            target_reviews = Review.objects.filter(movie_id=movie_id, rated=request.data.get('rated'))
            for review in target_reviews:
                user = get_object_or_404(User, pk=review.user_id)
                user.acc_point += 10
                user.curr_point += 10
                user.save()


            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        movie = get_object_or_404(Movie, pk=movie_id)
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
        

@api_view(['GET'])
def get_by_user(request, user_id):
    person = get_object_or_404(User, pk=user_id)
    reviews = person.review_set.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def reviews_get_update_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    if not request.user.review_set.filter(pk=review_id).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response({ 'id': review_id }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def recommend(request):
    user = get_object_or_404(User, pk=request.user.pk)
    people = user.followings.all()
    tmp = []
    for person in people:
        reviews = person.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        tmp += serializer.data
    if len(tmp) == 0:
        top_rated_reviews = Review.objects.order_by('-rated')[0:20]
        serializer = ReviewSerializer(top_rated_reviews, many=True)
        tmp += serializer.data
    return Response(tmp)


@api_view(['POST'])
def likes(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        liked = False
    else:
        review.like_users.add(request.user)
        liked = True
    return Response({'review_id': review.pk, 'liked': liked})


@api_view(['POST'])
def comments_create(request, review_id):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def comments_delete(request, review_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if not request.user.comment_set.filter(pk=comment_id).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
    comment.delete()
    return Response({ 'id': comment_id }, status=status.HTTP_204_NO_CONTENT)