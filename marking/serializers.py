from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = '__all__'

class ConvenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convener
        fields = '__all__'