from django.test import TestCase
from courses.models import Course


class CourseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a course
        test_course = Course.objects.create(
            title='test course title',
            description='test course description',
            start_date='2021-04-25',
            end_date='2021-05-05',
            lectures='10'
        )
        test_course.save()

    def test_course_content(self):
        course = Course.objects.get(id=1)
        title = f'{course.title}'
        description = f'{course.description}'
        start_date = f'{course.start_date}'
        end_date = f'{course.end_date}'
        lectures = f'{course.lectures}'
        self.assertEqual(title, 'test course title')
        self.assertEqual(description, 'test course description')
        self.assertEqual(start_date, '2021-04-25')
        self.assertEqual(end_date, '2021-05-05')
        self.assertEqual(lectures, '10')

    def test_post_coupse(self):
        course = Course.objects.create(
            title='some title',
            description='some description',
            start_date='2021-04-27',
            end_date='2021-05-17',
            lectures='17'
        )
        course.save()
