
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], url_path='add-student')
    def add_student(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')

        if not student_id:
            return Response({'error': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Verify student exists in Spring Boot microservice
        spring_url = f"http://localhost:8081/api/students/{student_id}"
        try:
            response = requests.get(spring_url, timeout=3)
        except requests.exceptions.RequestException:
            return Response({'error': 'Student service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        if response.status_code != 200:
            return Response({'error': 'Student not found in Student Service'}, status=status.HTTP_404_NOT_FOUND)

        # ✅ Student exists — add their ID to the list
        if student_id not in course.students:
            course.students.append(student_id)
            course.save()
            return Response({'message': f'Student {student_id} added to {course.name}.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': f'Student {student_id} is already enrolled in {course.name}.'}, status=status.HTTP_200_OK)
