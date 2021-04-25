from rest_framework import generics
from courses.models import Course
from django.db.models import Q
from courses.serializers import CoursesListSerializer, CourseDetailSerializer


class ListCourse(generics.ListCreateAPIView):
    serializer_class = CoursesListSerializer

    def get_queryset(self):
        queryset = Course.objects.all()

        start_date = self.request.GET.getlist('start_date')
        end_date = self.request.GET.getlist('end_date')

        if start_date:
            queryset = queryset.filter(start_date__in=start_date)

        if end_date:
            queryset = queryset.filter(end_date__in=end_date)

        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(Q(title__contains=query))

        return queryset


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
