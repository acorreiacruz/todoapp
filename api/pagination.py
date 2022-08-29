from rest_framework.pagination import BasePagination


class PaginacaoCustomizada(BasePagination):
    page_size = 6