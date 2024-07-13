from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Quiz, Question
from apps.results.models import Result
from .forms import QuizForm, QuestionForm, OptionForm


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quizzes/quiz_detail.html'
    context_object_name = 'quiz'


class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class QuizUpdateView(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz_list')


@login_required
def add_question(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('quiz_detail', pk=quiz.pk)
    else:
        form = QuestionForm()
    return render(request, 'quizzes/add_question.html', {'form': form})


@login_required
def add_option(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question = question
            option.save()
            return redirect('quiz_detail', pk=question.quiz.pk)
    else:
        form = OptionForm()
    return render(request, 'quizzes/add_option.html', {'form': form})


class ResultListView(ListView):
    model = Result
    template_name = 'results/result_list.html'
    context_object_name = 'results'

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)


class ResultDetailView(DetailView):
    model = Result
    template_name = 'results/result_detail.html'
    context_object_name = 'result'
