from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model # another way to import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","author","title","body","created_at")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model() # infact , it is User
        fields = ('id','username',)
