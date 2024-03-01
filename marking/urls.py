from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:urn>', views.studentPage, name='studentPage'),
    path('academic/<int:id>', views.academicPage, name='academicPage'),
    path('convener/<int:id>', views.convenerPage, name='convenerPage')
]