from django_filters import FilterSet
from .models import Project


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'category__category_name': ['icontains'],
            'budget': ['gte', 'lte'],
            'skills_required__skill_name': ['icontains'],
            'created_at': ['gte', 'lte'],
            'deadline': ['gte', 'lte'],
        }