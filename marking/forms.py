from django import forms
from . models import *

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

class Academic1Form(AcademicForm):
    def __init__(self, *args, **kwargs):
        super(Academic1Form, self).__init__(*args, **kwargs)
        self.fields['mark'].label = 'Academic 1 Mark'

class Academic2Form(AcademicForm):
    def __init__(self, *args, **kwargs):
        super(Academic2Form, self).__init__(*args, **kwargs)
        self.fields['mark'].label = 'Academic 2 Mark'

class ModerationForm(forms.ModelForm):
    class Meta: 
        model = Moderation
        fields = '__all__'