import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Quiz, Question, Option
from apps.results.models import Result
from .forms import QuizForm, QuestionForm, OptionForm, QuizAnswerForm


logger = logging.getLogger(__name__)


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quizzes = Quiz.objects.all()
        for quiz in quizzes:
            if not quiz.quiz_id:
                logger.warning(f'Quiz "{quiz.title}" has an invalid ID')
        context['quizzes'] = quizzes
        return context


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quizzes/quiz_detail.html'
    context_object_name = 'quiz'


@login_required
def start_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = QuizAnswerForm(request.POST, questions=questions)
        if form.is_valid():
            result = Result.objects.create(quiz_id=quiz, user_id=request.user, score=0)
            score = 0
            for question in questions:
                selected_option_id = form.cleaned_data[f'question_{question.question_id}']
                selected_option = Option.objects.get(pk=selected_option_id)
                if selected_option.is_correct:
                    score += 1
            result.score = score
            result.save()
            return redirect('quiz:quiz_result', pk=result.pk)
    else:
        form = QuizAnswerForm(questions=questions)
    return render(request, 'quizzes/start_quiz.html', {'quiz': quiz, 'form': form})


class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz:quiz_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class QuizUpdateView(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz:quiz_list')


@login_required
def add_question(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('quiz:quiz_detail', pk=quiz.pk)
    else:
        form = QuestionForm()
    return render(request, 'quizzes/add_question.html', {'form': form, 'quiz': quiz})


@login_required
def add_option(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question = question
            option.save()
            return redirect('quiz:quiz_detail', pk=question.quiz.pk)
    else:
        form = OptionForm()
    return render(request, 'quizzes/add_option.html', {'form': form, 'question': question})


class ResultListView(ListView):
    model = Result
    template_name = 'results/result_list.html'
    context_object_name = 'results'

    def get_queryset(self):
        return Result.objects.filter(user_id=self.request.user)


class ResultDetailView(DetailView):
    model = Result
    template_name = 'results/result_detail.html'
    context_object_name = 'result'


class QuizResultView(DetailView):
    model = Result
    template_name = 'quizzes/quiz_result.html'
    context_object_name = 'result'
