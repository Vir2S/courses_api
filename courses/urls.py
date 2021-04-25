from django.urls import path
from courses.views import ListCourse, DetailCourse

urlpatterns = [
    path('courses/', ListCourse.as_view()),
    path('courses/<int:pk>/', DetailCourse.as_view()),
]