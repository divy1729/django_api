from django.shortcuts import render
from rest_framework import viewsets
from api.models import Student
from api.serializers import StudentSerializers
# Create your views here.
class StudentviewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializers