from rest_framework.pagination import PageNumberPagination


class MySmallNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "sayfa"
    page_size_query_param = "adet"
    max_page_size = 100