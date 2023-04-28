from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer


def home(request):
    return HttpResponse('<h1>API Page</h1>')

#? HTTP methods -------->>>
# - GET (DB den veri çağırma, read)
# - POST (DB de değişiklik, create)
# - PUT (DB de değişiklik, update)
# - DELETE (DB de değişiklik, delete)
# - PATCH (DB de değişiklik, partially update)

@api_view(["GET"])
def student_api(request):
    student = Student.objects.all()  # data type : queryset
    serializer = StudentSerializer(student, many=True) # data type : querydict
    return Response(serializer.data)   # data type : JSON

@api_view(["POST"])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {"message": "Student successfully created.."}
        return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(["PATCH"])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        # message = {"message": "Student successfully updated.."}
        data = serializer.data
        data["message"] = "Student successfully updated.."
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    message = {"message": "Student successfully deleted.."}
    return Response(message, status=status.HTTP_200_OK)