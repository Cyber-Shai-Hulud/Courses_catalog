from rest_framework import serializers
from .models import Courses


# Proving way for serializing of our model into JSON
class CoursesListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='api:detail',
        lookup_field='id',
    )

    class Meta:
        model = Courses
        fields = ['detail_url', 'name', 'start_date', 'end_date', 'amount']


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
