from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import *
from posts.models import Group, Follow, Post


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Post (публикация)."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с моделью Group (группа поста)."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Comment (комментарий)."""

    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticated,
        IsAuthorOrReadOnly,
    )

    @property
    def requested_post(self):
        return get_object_or_404(
            Post, pk=self.kwargs.get('post_id')
        )

    def perform_create(self, serializer):
        serializer.save(
            post=self.requested_post,
            author=self.request.user
        )

    def get_queryset(self):
        return self.requested_post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Follow (подписка)."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer