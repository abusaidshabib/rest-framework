from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    # converting complex data into python data
    serializer = StudentSerializer(stu)
    # Converting Python data to JSON data
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')

# Create your views here.
def student_list(request, pk):
    stu = Student.objects.get(id=pk)
    # converting complex data into python data
    serializer = StudentSerializer(stu)
    # Converting Python data to JSON data
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')