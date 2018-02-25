# Reference:https://docs.djangoproject.com/en/1.11/intro/
from django.contrib import admin

from .models import Choice, Questions,Gender, Age, Education, Religion, Ethnicity, Income, Constituency
#Editing the admin page

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class GenderInline(admin.TabularInline):
    model = Gender
    extra = 1

class AgeInline(admin.TabularInline):
    model = Age
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ReligionInline(admin.TabularInline):
    model = Religion
    extra = 1

class EthnicityInline(admin.TabularInline):
    model = Ethnicity
    extra = 1

class IncomeInline(admin.TabularInline):
    model = Income
    extra = 1

class ConstituencyInline(admin.TabularInline):
    model = Constituency
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline, GenderInline, AgeInline, EducationInline, ReligionInline, EthnicityInline,IncomeInline,ConstituencyInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Questions, QuestionAdmin)