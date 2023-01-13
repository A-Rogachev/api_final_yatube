from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель сообщества."""

    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Укажите название группы',
    )
    slug = models.SlugField(
        verbose_name='Slug для url-адреса',
        help_text='Укажите slug для url-адреса группы',
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Добавьте описание группы',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        """Возвращает название группы"""
        return self.title


class Post(models.Model):
    """Модель сообщения (публикация блога)."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )


    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментария для публикации."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Модель подписки."""

    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        related_name='follower',
        on_delete=models.CASCADE,
    )

    following = models.ForeignKey(
        User,
        verbose_name='Автор контента',
        related_name='following',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique follow'
            ),
            models.CheckConstraint(
                name='prevent_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
        ]

    def __str__(self) -> str:
        """Строковое представление подписки"""
        return f'{self.user} подписан на {self.following}'
