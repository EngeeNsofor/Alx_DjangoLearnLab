from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsOwnerOrReadOnly()]
        return [permissions.IsAuthenticatedOrReadOnly()]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), permissions.IsOwnerOrReadOnly()]
        return [permissions.IsAuthenticatedOrReadOnly()]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Define the queryset for the Post model
    serializer_class = PostSerializer  # Define the serializer to use for Post model
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_fields = ['title', 'content']  # Fields that can be filtered
