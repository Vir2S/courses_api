from django_filters import rest_framework as filters
from rest_framework import filters as search_filters
from rest_framework import generics
from django.db.models import Q
from courses.serializers import CoursesListSerializer, CourseDetailSerializer
from courses.models import Course
from courses.filters import CourseFilter


class ListCourse(generics.ListAPIView):
    serializer_class = CoursesListSerializer
    search_fields = ['title']
    filter_backends = (filters.DjangoFilterBackend, search_filters.SearchFilter)
    filterset_class = CourseFilter

    def get_queryset(self):
        queryset = Course.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(Q(title__contains=query))

        return queryset


class CreateCourse(generics.CreateAPIView):
    # queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
