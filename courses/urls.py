from django.urls import path
from courses.views import ListCourse, DetailCourse

urlpatterns = [
    path('', ListCourse.as_view()),
    path('<int:pk>/', DetailCourse.as_view()),
]