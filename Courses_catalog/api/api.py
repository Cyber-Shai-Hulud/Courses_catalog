from .models import Courses
from rest_framework import viewsets, permissions
from .serializers import CoursesSerializer


# View
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoursesSerializer
