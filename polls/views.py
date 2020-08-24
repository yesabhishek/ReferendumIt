from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

class HomeView(ListView):
  model = Question
   
  template_name = 'polls/home.html'  # app/model_viewtype.html
  
  
  """ ordering = ['-date_posted'] """

class DetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'polls/details.html'
    login_url = '/login/'
    redirect_field_name = 'details'

    
class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'
    login_url = '/login/'
    redirect_field_name = 'results'

@login_required
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})  

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def get_queryset(self):
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


""" def get_index(request):
    return render(request, template_name='polls/index.html') """

