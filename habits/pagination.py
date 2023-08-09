from rest_framework.pagination import PageNumberPagination


class MabbitsPaginator(PageNumberPagination):
    page_size = 5

