from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from notifications.models import Notification
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()  # Get all users this user is following

        # Retrieve posts from the followed users, ordered by the most recent first
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikePostView(generics.GenericAPIView):
    """
    Endpoint to allow a user to like a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Fetch the post using get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)

        # Create or retrieve the like instance
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a notification for the post owner (if it's not the same user)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"success": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    """
    Endpoint to allow a user to unlike a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Fetch the post using get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)

        # Attempt to find the like instance
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()
        return Response({"success": "Post unliked successfully."}, status=status.HTTP_200_OK)
