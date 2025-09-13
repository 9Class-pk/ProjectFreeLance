from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'role', 'bio', 'avatar', 'skills', 'social_links')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    skills_required = SkillSerializer(many=True, read_only=True)
    client = UserProfileSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    freelancer = UserProfileSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserProfileSerializer(read_only=True)
    target = UserProfileSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
