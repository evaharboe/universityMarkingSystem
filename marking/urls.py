from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:urn>', views.StudentPage, name='studentPage'),
    path('academic/<int:id>', views.AcademicPage, name='academicPage'),
    path('convener/<int:id>', views.ConvenerPage, name='convenerPage'),
    path('moderation/<int:id>', views.ModerationPage, name='moderationPage'),
]