from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MySmallNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "sayfa"
    page_size_query_param = "adet"
    max_page_size = 100
    
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5 
    limit_query_param = "how_many"
    

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = "-first_name"