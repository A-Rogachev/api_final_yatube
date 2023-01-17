from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

from .validators import NotFollowSelfValidator
from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post (публикация)."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment (комментарий)."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group (группа поста)."""

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow (подписка на автора)."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        read_only=False,
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    validators = [
        validators.UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following'],
        ),
        NotFollowSelfValidator(
            fields=['user', 'following'],
            message='Нельзя подписаться на самого себя!',
        )
    ]
