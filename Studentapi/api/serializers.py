from rest_framework import serializers
from api.models import Student

from api.models import Student
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields="__all__"