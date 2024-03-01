from django import forms
from .models import *

class ConvenerSelectionForm(forms.ModelForm):
    class Meta:
        model = Convener
        fields = ['selected_student', 'academic1', 'academic2']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
        'keywords': forms.Select(choices=Student.KEYWORD_CHOICES)
    }
        
class AcademicForm(forms.ModelForm):
    class Meta:
        model = Bridge
        fields = '__all__'
    
    def __init__(self, academic, *args, **kwargs):
        super(AcademicForm, self).__init__(*args, **kwargs)
        self.fields['urn'].queryset = Bridge.objects.filter(academicId=academic)