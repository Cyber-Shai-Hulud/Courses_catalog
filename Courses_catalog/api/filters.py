from .models import Courses
from django_filters import DateFilter, FilterSet


class CoursesFilter(FilterSet):
    start_date = DateFilter(lookup_expr='start')
    end_date = DateFilter(lookup_expr='end')

    class Meta:
        model = Courses
        fields = ['start_date', 'end_date']
