from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_api(reques):
    # student = Student.objects.get(id=int(id))


#  if request.method == 'GET':
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     pythondata = JSONParser().parse(stream)
#     id = pythondata.get('id',None)
#     if id is not None:
#       stu = Student.objects.get(id=id)
#       serializer = StudentSerializer(stu)
#       json_data = JSONRenderer().render(serializer.data)
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return HttpResponse(serializer.data)
    # stu = Student.object.all()
    # serializer = StudentSerializer(stu, many=True)
