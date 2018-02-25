# Reference:https://docs.djangoproject.com/en/1.11/intro/
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from polls.forms import MyModelForm
from .models import Choice, Questions, Constituency


#Different views
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Questions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions, Constituency
    #form_class = MyModelForm
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Questions.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'


def vote(request, question_id):
    questions = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = questions.choice_set.get(pk=request.POST['choice'])
        selected_gender = questions.gender_set.get(pk=request.POST['gender'])
        selected_age = questions.age_set.get(pk=request.POST['age'])
        selected_education = questions.education_set.get(pk=request.POST['education'])
        selected_religion= questions.religion_set.get(pk=request.POST['religion'])
        selected_ethnicity = questions.ethnicity_set.get(pk=request.POST['ethnicity'])
        selected_income = questions.income_set.get(pk=request.POST['income'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': questions,
            'error_message': "You didn't select anything.",
        })
    else:
        selected_choice.votes += 1
        selected_gender.num += 1
        selected_age.option += 1
        selected_education.number += 1
        selected_religion.pick += 1
        selected_ethnicity.racenum += 1
        selected_income.amount += 1
        selected_choice.save()
        selected_gender.save()
        selected_age.save()
        selected_education.save()
        selected_religion.save()
        selected_ethnicity.save()
        selected_income.save()
        return HttpResponseRedirect(reverse('polls:results', args=(questions.id,)))