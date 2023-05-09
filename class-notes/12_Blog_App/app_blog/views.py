from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# class FixView(ModelViewSet):
#     pass

class BlogCategoryView(ModelViewSet):
    queryset=BlogCategory.objects.all()
    serializer_class=BlogCategorySerializer

class BlogPostView(ModelViewSet):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    # blogpotview ın inherit odildiği class taki fonk. override yaptık
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.viewed +=1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
       

class BlogCommentView(ModelViewSet):
    queryset=BlogComment.objects.all()
    serializer_class=BlogCommentSerializer