# Reference:https://docs.djangoproject.com/en/1.11/intro/
import datetime
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
#For time zone
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#The choices
class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
#what gender the voter is
class Gender(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    gender_text = models.CharField(max_length=250)
    num = models.IntegerField(default=0)
    def __str__(self):
            return self.gender_text

#what age the voter is
class Age(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    age_text = models.CharField(max_length=250)
    option = models.IntegerField(default=0)
    def __str__(self):
            return self.age_text

#what level of education the voter has
class Education(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    education_text = models.CharField(max_length=250)
    number = models.IntegerField(default=0)
    def __str__(self):
            return self.education_text

#what religion the voter is
class Religion(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    religion_text = models.CharField(max_length=250)
    pick = models.IntegerField(default=0)
    def __str__(self):
            return self.religion_text

#what ethnicity the voter is
class Ethnicity(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    ethnicity_text = models.CharField(max_length=250)
    racenum = models.IntegerField(default=0)
    def __str__(self):
            return self.ethnicity_text

#what income the voter has
class Income (models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    income_text = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)
    def __str__(self):
            return self.income_text

#what Constituency the voter is in
class Constituency (models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    constituency_text = models.CharField(max_length=250)
    intensity = models.IntegerField(default=0)
    def __str__(self):
            return self.constituency_text