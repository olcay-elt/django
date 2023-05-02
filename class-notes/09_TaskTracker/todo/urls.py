from django.urls import path,include
from .views import welcome,todo_list_create

urlpatterns = [
    path('', welcome),
    #fbv
    path('todos/',todo_list_create)
]