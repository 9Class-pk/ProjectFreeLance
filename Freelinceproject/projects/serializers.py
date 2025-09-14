from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken

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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception:
            self.fail("bad_token")