from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followings = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'acc_point', 'curr_point', 'followings',)
