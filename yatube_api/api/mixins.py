from rest_framework import mixins, viewsets


class CreateListViewset(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Вьюсет позволяющий делать GET и POST запросы."""

    pass
