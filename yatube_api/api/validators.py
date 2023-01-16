from rest_framework import serializers


class NotFollowSelfValidator:
    """Валидатор для предотвращение подписки на самого себя."""

    message = 'Ошибка - неуникальные значения в списке переданных.'
    requires_context = True

    def __init__(self, model_fields, message=None):
        self.model_fields = model_fields
        self.message = message or self.message

    def __call__(self, attrs, serializer):
        field_names = [
            field.name for field in self.model_fields
        ]
        different_field_values = set(
            [attrs[key] for key in attrs.keys() if key in field_names]
        )
        if len(attrs) != len(different_field_values):
            raise serializers.ValidationError(self.message)

    def __repr__(self):
        return '<%s(model_fields=%s, message=%s)>' % (
            self.__class__.__name__,
            self.model_fields,
            self.message
        )
