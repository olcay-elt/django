from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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

###############################################################
@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()  # queryset (complex data types)
        serializer = StudentSerializer(students, many=True) # python data types (dict , querydict)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)
    
    
#!################### CLASS VIEWS  ###########################################

#! APIView class
class StudentListCreate(APIView):
    
    def get(self, request):
        student = Student.objects.all()  # data type : queryset
        serializer = StudentSerializer(student, many=True) # data type : querydict
        return Response(serializer.data)   # data type : JSON
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "Student successfully created.."}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    
    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data),
    
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # message = {"message": "Student successfully updated.."}
            data = serializer.data
            data["message"] = "Student successfully updated.."
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        message = {"message": "Student successfully deleted.."}
        return Response(message, status=status.HTTP_200_OK)