from django_filters import rest_framework as filters
from courses.models import Course


class CourseFilter(filters.FilterSet):

    start_date_from = filters.DateFilter(field_name="start_date", lookup_expr='gte')
    start_date_to = filters.DateFilter(field_name="start_date", lookup_expr='lte')

    end_date_from = filters.DateFilter(field_name='end_date', lookup_expr='gte')
    end_date_to = filters.DateFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Course
        fields = [
            'start_date',
            'end_date',
            'start_date_from',
            'start_date_to',
            'end_date_from',
            'end_date_to',
        ]

