from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.
def welcome(request):
    return HttpResponse(
        '<h1 style="background-color: brown;"> welcome </>'
    
    )

@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method=='GET':
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def todo_get_update_delete(request):
    if request.method=='GET':
        todo=get_object_or_404(Todo,id=id)
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method=='PUT':
        
        pass
    elif request.method=='DELETE':
        pass    
    