from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .mixins import CreateListViewset
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Group, Post





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
        IsAuthorOrReadOnly,
    )

    @property
    def requested_post(self):
        return get_object_or_404(
            Post, pk=self.kwargs.get('post_id'),
        )

    def perform_create(self, serializer):
        serializer.save(
            post=self.requested_post,
            author=self.request.user,
        )

    def get_queryset(self):
        return self.requested_post.comments.all()


class FollowViewSet(CreateListViewset):
    """Вьюсет для работы с моделью Follow (подписка)."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('=following__username', )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
