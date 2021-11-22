from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer 
from .models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def follow(request, user_id):
    me = request.user
    you = get_object_or_404(User, pk=user_id)
    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
        return Response({ 'id': you.id }, status=status.HTTP_204_NO_CONTENT)
    return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(User, username=username)
    data={
    'followers_cnt': person.followers.all().count(),
    'followings_cnt': person.followings.all().count()
    }
    serializer = UserSerializer(person)
    # serializer에 추가 데이터 만들어서 보내기
    data.update(serializer.data)
    return Response(data)


@api_view(['GET'])
def get(request):
    user = request.user
    serializer = UserSerializer(user)
    data = {
        'level': user.acc_point // 100
    }
    data.update(serializer.data)
    return Response(data)