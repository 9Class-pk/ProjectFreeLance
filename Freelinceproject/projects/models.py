from django.db import models
from django.contrib.auth.models import AbstractUser


class Skill(models.Model):
    skill_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill_name


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='users', blank=True)
    social_links = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    skills_required = models.ManyToManyField(Skill, related_name='projects', blank=True)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='offers')
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='offers')
    message = models.TextField()
    proposed_budget = models.DecimalField(max_digits=12, decimal_places=2)
    proposed_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Offer by {self.freelancer.username} for {self.project.title}'


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='given_reviews')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review {self.rating} by {self.reviewer.username}'
