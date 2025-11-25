from django.test import TestCase
from courses.models import Course


class ContextLoadTest(TestCase):
    """
    Equivalent to Spring Boot's contextLoads().
    If this test runs, Django context is loaded successfully.
    """
    def test_context_loads(self):
        self.assertTrue(True)


class CourseRepositoryTest(TestCase):
    """
    Equivalent of Spring Boot repository tests:
    - shouldSaveStudent()
    - shouldFindAllStudents()
    """

    def test_should_save_course(self):
        # Create a new Course entry
        course = Course.objects.create(
            name="Python Basics",
            instructor="John Doe",
            category="Programming",
            schedule_day="Monday",
            schedule_time="10:00",
            students=[1, 2, 3]  # example student IDs
        )

        # Assert exactly one record exists
        self.assertEqual(Course.objects.count(), 1)

    def test_should_find_all_courses(self):
        # Insert 1 record
        Course.objects.create(
            name="Python Basics",
            instructor="John Doe",
            category="Programming",
            schedule_day="Monday",
            schedule_time="10:00",
            students=[1, 2, 3]
        )

        # Retrieve all courses
        courses = Course.objects.all()

        # Validate count
        self.assertEqual(courses.count(), 1)

        # Validate field values
        course = courses.first()
        self.assertEqual(course.name, "Python Basics")
        self.assertEqual(course.instructor, "John Doe")
        self.assertEqual(course.category, "Programming")
        self.assertEqual(course.schedule_day, "Monday")
        self.assertEqual(course.students, [1, 2, 3])
