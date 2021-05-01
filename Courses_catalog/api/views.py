from .serializers import CoursesSerializer, CoursesListSerializer
from .models import Courses
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CoursesFilter


class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    lookup_url_kwarg = 'id'


class CoursesListView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filter_class = CoursesFilter
