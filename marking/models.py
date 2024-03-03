from django.db import models
from django import forms
from django.shortcuts import get_object_or_404

       
class Student(models.Model):
    urn = models.IntegerField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    moderation = models.OneToOneField('Moderation', on_delete=models.CASCADE, null=True, blank=True, related_name='student_entry')
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

class Moderation(models.Model):
    urn = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='moderation_entry')
    finalMark = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.urn} - Final Mark: {self.finalMark}"

class Academic(models.Model):
    academicId = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return str(self.forename) + " " + str(self.surname)

class Bridge(models.Model):
    urn = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic1 = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='academic1', default=0)
    academic2 = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='academic2', default=0)
    mark1 = models.FloatField(default=0.0)
    mark2 = models.FloatField(default=0.0)
    comment = models.TextField(default= "Add comment")

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

    def calculateAvg(self, *args, **kwargs):
        bridge1 = get_object_or_404(Bridge, urn=self.selected_student, academic1=self.academic1)
        bridge2 = get_object_or_404(Bridge, urn=self.selected_student, academic2=self.academic2)
        
        averageMark = (bridge1.mark1 + bridge2.mark2) / 2
        difference = abs(bridge1.mark1-bridge2.mark2)

        ##on boundary
        if 39 <= averageMark <= 70 and averageMark % 10 == 9:
            print("Needs moderation")

        ##larger than 10% mark difference
        if difference > 0.1 * averageMark:
            print("Needs moderation")

        super(Convener, self).save(*args, **kwargs)
    
