from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly, IsUserOrReadOnly

from django.contrib.auth import get_user_model

from rest_framework import viewsets
# Create your views here.
class PostList(generics.ListCreateAPIView):
    """
    Description of this endpoint
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

'''
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)
'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,) # this still works well with ViewSet for Custom Permission
