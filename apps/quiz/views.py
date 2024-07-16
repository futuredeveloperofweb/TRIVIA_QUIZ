import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from apps.results.models import Result

from .forms import OptionForm, QuestionForm, QuizAnswerForm, QuizForm
from .models import Option, Question, Quiz

# Initialize logger
logger = logging.getLogger(__name__)


class QuizListView(ListView):
    """View for listing all quizzes."""

    model = Quiz
    template_name = "quizzes/quiz_list.html"
    context_object_name = "quizzes"

    def get_context_data(self, **kwargs):
        """Add additional context to the view."""
        context = super().get_context_data(**kwargs)
        quizzes = Quiz.objects.all()
        for quiz in quizzes:
            if not quiz.quiz_id:
                logger.warning(f'Quiz "{quiz.title}" has an invalid ID')
        context["quizzes"] = quizzes
        return context


class QuizDetailView(DetailView):
    """View for displaying a single quiz."""

    model = Quiz
    template_name = "quizzes/quiz_detail.html"
    context_object_name = "quiz"


@login_required
def start_quiz(request, pk):
    """Handle starting a quiz and submitting answers.

    Args:
        request: The HTTP request object.
        pk: The primary key of the quiz.

    Returns:
        HttpResponse: The rendered quiz page or a redirect to the quiz result page.
    """
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    if request.method == "POST":
        form = QuizAnswerForm(request.POST, questions=questions)
        if form.is_valid():
            result = Result.objects.create(quiz_id=quiz, user_id=request.user, score=0)
            score = 0
            for question in questions:
                selected_option_id = form.cleaned_data[
                    f"question_{question.question_id}"
                ]
                selected_option = Option.objects.get(pk=selected_option_id)
                if selected_option.is_correct:
                    score += 1
            result.score = score
            result.save()
            logger.info(
                f"Quiz submitted by user {request.user.username} with score {score}"
            )
            return redirect("quiz:quiz_result", pk=result.pk)
    else:
        form = QuizAnswerForm(questions=questions)
    return render(request, "quizzes/start_quiz.html", {"quiz": quiz, "form": form})


class QuizCreateView(CreateView):
    """View for creating a new quiz."""

    model = Quiz
    form_class = QuizForm
    template_name = "quizzes/quiz_form.html"
    success_url = reverse_lazy("quiz:quiz_list")

    def form_valid(self, form):
        """Handle the form validation."""
        form.instance.created_by = self.request.user
        logger.info(f"Quiz created by {self.request.user.username}")
        return super().form_valid(form)


class QuizUpdateView(UpdateView):
    """View for updating an existing quiz."""

    model = Quiz
    form_class = QuizForm
    template_name = "quizzes/quiz_form.html"
    success_url = reverse_lazy("quiz:quiz_list")


@login_required
def add_question(request, pk):
    """Handle adding a question to a quiz.

    Args:
        request: The HTTP request object.
        pk: The primary key of the quiz.

    Returns:
        HttpResponse: The rendered add question page or a redirect to the quiz detail page.
    """
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz_id = quiz
            question.save()
            logger.info(
                f"Question added to quiz {quiz.title} by {request.user.username}"
            )
            return redirect("quiz:quiz_detail", pk=quiz.pk)
    else:
        form = QuestionForm()
    return render(request, "quizzes/add_question.html", {"form": form, "quiz": quiz})


@login_required
def add_option(request, pk):
    """Handle adding an option to a question.

    Args:
        request: The HTTP request object.
        pk: The primary key of the question.

    Returns:
        HttpResponse: The rendered add option page or a redirect to the quiz detail page.
    """
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question_id = question
            option.save()
            logger.info(
                f"Option added to question {question.question_text} by {request.user.username}"
            )
            return redirect("quiz:quiz_detail", pk=question.quiz_id.pk)
    else:
        form = OptionForm()
    return render(
        request, "quizzes/add_option.html", {"form": form, "question": question}
    )


class ResultListView(ListView):
    """View for listing all results of the logged-in user."""

    model = Result
    template_name = "results/result_list.html"
    context_object_name = "results"

    def get_queryset(self):
        """Filter the results by the logged-in user."""
        return Result.objects.filter(user_id=self.request.user)


class ResultDetailView(DetailView):
    """View for displaying a single quiz result."""

    model = Result
    template_name = "results/result_detail.html"
    context_object_name = "result"


class QuizResultView(DetailView):
    """View for displaying the result of a completed quiz."""

    model = Result
    template_name = "quizzes/quiz_result.html"
    context_object_name = "result"
