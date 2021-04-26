from rest_framework import generics
from django.db.models import Q
from courses.serializers import CoursesListSerializer, CourseDetailSerializer
from courses.models import Course


class ListCourse(generics.ListCreateAPIView):
    serializer_class = CoursesListSerializer

    def get_queryset(self):
        queryset = Course.objects.all()

        start_date = self.request.GET.getlist('start_date')
        end_date = self.request.GET.getlist('end_date')

        if start_date:
            queryset = queryset.filter(start_date__range=start_date)

        if end_date:
            queryset = queryset.filter(end_date__range=end_date)

        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(Q(title__contains=query))

        return queryset


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
