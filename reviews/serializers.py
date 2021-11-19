from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'acc_point',)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'content', 'rated','like_cnt', 'user',)
