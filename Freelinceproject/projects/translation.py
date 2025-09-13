from .models import UserProfile, Category, Project, Offer, Skill, Review
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('bio',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('project_name', 'description', )

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ('message',  )

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',  )

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('skill_name',  )

