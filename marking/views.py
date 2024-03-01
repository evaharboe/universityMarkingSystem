from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import *

@api_view(['POST'])
def studentPage(request, urn):

    try:
        student = Student.objects.get(pk=urn)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
    else:
        form = StudentForm(instance=student)
    return render(request, 'htmlNAME', {'student': student, 'form': form})

@api_view(['POST'])
def academicPage(request, academicId):

    try:
        academic = Academic.objects.get(pk=academicId)
    except Academic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        form1 = Academic1Form(request.POST, prefix = 'academic1')
        form2 = Academic2Form(request.POST, prefix = 'academic2')
        if form1.is_valid() and form2.isValid():
            form1.save()
            form2.save()
    else:
        form1 = Academic1Form(prefix = 'academic1')
        form2 = Academic2Form(prefix = 'academic2')
    
    return render(request, 'HTML NAME', {'form1': form1, 'form2': form2})

    
    
@api_view(['POST'])
def ConvenerPage(request, convenerId):

    try:
        convener = Convener.objects.get(pk=convenerId)
    except Convener.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        form = ConvenerSelectionForm(request.POST, instance = convener)
        if form.is_valid():
            selected_student = form.cleaned_data['selected_student']
            academic1 = form.cleaned_data['academic1']
            academic2 = form.cleaned_data['academic2']

            if academic1 != academic2:
                Bridge.objects.create(urn=selected_student, academicId=academic1, mark=0)
                Bridge.objects.create(urn=selected_student, academicId=academic2, mark=0)
    else:
        form = ConvenerSelectionForm(instance=convener)
    
    return render(request, 'HTML NAME', {'form': form})


