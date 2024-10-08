
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import QuestionForm
from .models import Choice, Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('polls:index')
    else:
        form = AuthenticationForm()

    return render(request, 'polls/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('polls:index')

@login_required
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})


def statistics_view(request):
    total_questions = Question.total_questions()
    total_choices = Question.total_choices()
    total_votes = Question.total_votes()
    average_votes = Question.average_votes()
    most_popular = Question.most_popular()
    least_popular = Question.least_popular()
    latest_question = Question.latest_question()

    context = {
        'total_questions': total_questions,
        'total_choices': total_choices,
        'total_votes': total_votes,
        'average_votes': average_votes,
        'most_popular': most_popular,
        'least_popular': least_popular,
        'latest_question': latest_question,
    }
    return render(request, 'polls/statistics.html', context)


class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"
    pk_url_kwarg = 'question_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context['choices'] = question.get_choices()
        return context

class AllPollsView(generic.ListView):
    template_name = 'polls/all_polls.html'
    context_object_name = 'all_questions'

    def get_queryset(self):
        """Retourne tous les sondages classés par date de publication"""
        return Question.objects.order_by("-pub_date")

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
               :5
               ]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))