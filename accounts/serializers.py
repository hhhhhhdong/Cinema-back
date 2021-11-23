from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Scoreboard

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # 회원가입시 팔로잉정보를 받지 않기위해 추가
    followings = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'acc_point', 'curr_point', 'followings',)

class ScoreboardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    genre = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Scoreboard
        fields = ('id', 'user', 'genre', 'score',)