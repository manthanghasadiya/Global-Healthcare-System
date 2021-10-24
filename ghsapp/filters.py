from django.contrib.auth.models import User
from .models import doctorInfo
import django_filters


class doctor_filter(django_filters.FilterSet):
    class Meta():
        model = doctorInfo
        fields = ['degree_type', 'specialities_type']
