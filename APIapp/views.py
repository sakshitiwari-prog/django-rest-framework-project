import json
from django.shortcuts import render
from .models import Student
from .serializers import SerilaizersStudent
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
#model object-single student data
def student_detail(request,i):
    stu=Student.objects.get(id=i)
    # print(stu)
    # print('stu')
    serializer=SerilaizersStudent(stu)
    # print('serializer')
    # print(serializer)
    # print('serializer.data')
    # print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    # print('json_data')
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')
# query-set -all student data
def student_LIST(request):
    stu=Student.objects.all()
    serializer=SerilaizersStudent(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

