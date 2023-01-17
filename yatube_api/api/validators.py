from rest_framework import serializers


class NotFollowSelfValidator:
    """Валидатор для предотвращение подписки на самого себя."""

    message = 'Ошибка - неуникальные значения в списке переданных.'
    requires_context = True

    def __init__(self, fields, message=None):
        self.fields = fields
        self.message = message or self.message

    def __call__(self, attrs, serializer):
        different_field_values = {
            value for value in attrs.values()
        }
        if len(attrs) != len(different_field_values):
            raise serializers.ValidationError(self.message)

    def __repr__(self):
        return '<%s(model_fields=%s, message=%s)>' % (
            self.__class__.__name__,
            self.fields,
            self.message
        )
