from rest_framework import serializers
from courses.models import Course


class CoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', )
        # fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
