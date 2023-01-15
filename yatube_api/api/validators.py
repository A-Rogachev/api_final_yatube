from django.shortcuts import get_object_or_404
from rest_framework import serializers

from posts.models import User


class NotFollowSelfValidator:
    """Валидатор для предотвращение подписки на самого себя."""

    message = 'Нельзя подписаться на самого себя!'
    requires_context = True

    def __init__(self, message=None):
        self.message = message or self.message

    def __call__(self, attrs, serializer):
        user = serializer.context['request'].user
        following = get_object_or_404(
            User, username=serializer.initial_data.get('following')
        )
        if user == following:
            print(self)
            raise serializers.ValidationError(self.message)

    def __repr__(self):
        return '<%s(message=%s)>' % (
            self.__class__.__name__,
            self.message
        )
