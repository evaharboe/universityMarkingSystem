from django.db import models
from django import forms

# Create your models here.
class Student(models.Model):
    urn = models.IntegerField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    KEYWORD_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('ML', 'Machine Learning'),
        ('SE', 'Software Engineering'),
        ('DS', 'Data Science'),
        ('CS', 'Cyber Security'),
        ('IS', 'Information Systems'),
        ('CG', 'Computer Graphics'),
        ('HCI', 'Human Computer Interaction'),
        ('CV', 'Computer Vision'),
        ('NLP', 'Natural Language Processing'),
    ]
    keywords = models.CharField(max_length=50, choices=KEYWORD_CHOICES, default='select')

    def __str__(self):
        return self.forename + " " + self.surname

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    
    widgets = {
        'keywords': forms.Select(choices=Student.KEYWORD_CHOICES)
    }

class Academic(models.Model):
    academicId = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return str(self.forename) + " " + str(self.surname)

class Bridge(models.Model):
    urn = models.ForeignKey(Student, on_delete=models.CASCADE)
    academicId = models.ForeignKey(Academic, on_delete=models.CASCADE)
    mark = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['urn', 'academicId'], name='unique_bridge')
        ]

    def __str__(self):
        return str(self.urn) + " " + str(self.academicId)

class Convener(models.Model):
    convenerId = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return str(self.forename) + " " + str(self.surname)