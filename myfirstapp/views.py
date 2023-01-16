from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# from rest_framework.response import JSONResponse

# Create your views here.
def student_detail(request, pk):
  stu = Student.objects.get(id = pk)
  create = Student.objects.create()
#   print(stu)
#   stu = Student.objects.get()
  serializer = StudentSerializer(stu)
  json_data = JSONRenderer().render(serializer.data)
  return HttpResponse(json_data)
#   Query Set - All Student Data
def student_list(request):
  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  json_data = JSONRenderer().render(serializer.data)
  return HttpResponse(json_data)

  