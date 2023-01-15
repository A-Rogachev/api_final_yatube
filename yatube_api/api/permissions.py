from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение на изменение объекта только для автора."""

    def has_permission(self, request, view):
        "Незарегистрированный пользователь имеет право на чтение."
        return (request.method in permissions.SAFE_METHODS
                or not request.user.is_anonymous)

    def has_object_permission(self, request, view, obj):
        """Пользователь, не являющийся автором, не может изменять объект."""
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
