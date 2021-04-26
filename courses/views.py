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

        start_between = self.request.GET.getlist('start_between')
        end_between = self.request.GET.getlist('end_between')

        if start_date:
            queryset = queryset.filter(start_date__in=start_date)

        if end_date:
            queryset = queryset.filter(end_date__in=end_date)

        if start_between:
            queryset = queryset.filter(start_date__range=start_between)

        if end_between:
            queryset = queryset.filter(end_date__range=end_between)

        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(Q(title__contains=query))

        return queryset


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
