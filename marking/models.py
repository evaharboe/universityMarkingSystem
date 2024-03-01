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

class Academic(models.Model):
    academicId = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return str(self.forename) + " " + str(self.surname)

class Bridge(models.Model):
    urn = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic1 = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='academic1')
    academic2 = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='academic2')
    mark1 = models.FloatField()
    mark2 = models.FloatField()
    comment = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['urn', 'academic1'], name='unique_bridge_academic1'),
            models.UniqueConstraint(fields=['urn', 'academic2'], name='unique_bridge_academic2')
        ]

    def __str__(self):
        return f"{self.urn} - Academic 1: {self.mark1}, Academic 2: {self.mark2}"

class Convener(models.Model):
    convenerId = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    selected_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='selected_by_convener')
    academic1 = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='academic1_convener')
    academic2 = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='academic2_convener')

    def __str__(self):
        return str(self.forename) + " " + str(self.surname)