from django.urls import path
from .views import StudentViews, AboutStudentView


urlpatterns = [
    path('student/', StudentViews.as_view(), name='student'),
    path('about_student/<int:id>', AboutStudentView.as_view(), name='about_student'),
]
