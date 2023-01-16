from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import myapp,Employee
from myapp.serializers import Companyserializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views import View
# Create your views here.
from django.http import HttpResponse, JsonResponse 

# def index(request):
#     print("home page requested")
#     friends=[
#         'ankit',
#         'ravi',
#         'uttam'
#     ]
#     return JsonResponse(friends,safe=False)
class myappViewSet(viewsets.ModelViewSet):
    queryset= myapp.objects.all()
    serializer_class=Companyserializer
    @action(detail=True,methods=['GET'])
    def employees(self,request,pk=None):
        try:
           # print("get employees of",pk, "myapp")
           myapp=myapp.objects.get(pk=pk)
           emps=Employee.objects.filter(myapp=myapp)
           emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
           return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'hello'})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer
class Student(View):
    def get(self, request):
        queryset= StudentsForm.objects.all()
        # <view logic>
        return HttpResponse('result')