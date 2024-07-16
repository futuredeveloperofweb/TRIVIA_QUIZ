from django.urls import path

from .views import (
    QuizCreateView,
    QuizDetailView,
    QuizListView,
    QuizResultView,
    QuizUpdateView,
    ResultDetailView,
    ResultListView,
    add_option,
    add_question,
    start_quiz,
)

app_name = "quiz"


urlpatterns = [
    path("", QuizListView.as_view(), name="quiz_list"),
    path("<int:pk>/", QuizDetailView.as_view(), name="quiz_detail"),
    path("new/", QuizCreateView.as_view(), name="quiz_create"),
    path("<int:pk>/edit/", QuizUpdateView.as_view(), name="quiz_edit"),
    path("<int:pk>/add_question/", add_question, name="add_question"),
    path("question/<int:pk>/add_option/", add_option, name="add_option"),
    path("results/", ResultListView.as_view(), name="result_list"),
    path("result/<int:pk>/", ResultDetailView.as_view(), name="result_detail"),
    path("<int:pk>/start/", start_quiz, name="start_quiz"),
    path("result/<int:pk>/", QuizResultView.as_view(), name="quiz_result"),
]
