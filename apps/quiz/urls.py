from django.urls import path
from .views import (
    QuizListView,
    QuizDetailView,
    QuizCreateView,
    QuizUpdateView,
    add_question,
    add_option,
    ResultListView,
    ResultDetailView,
)

app_name = 'quiz'


urlpatterns = [
    path("", QuizListView.as_view(), name="quiz_list"),
    path("quiz/<int:pk>/", QuizDetailView.as_view(), name="quiz_detail"),
    path("quiz/new/", QuizCreateView.as_view(), name="quiz_create"),
    path("quiz/<int:pk>/edit/", QuizUpdateView.as_view(), name="quiz_edit"),
    path("quiz/<int:pk>/add_question/", add_question, name="add_question"),
    path("question/<int:pk>/add_option/", add_option, name="add_option"),
    path("results/", ResultListView.as_view(), name="result_list"),
    path("result/<int:pk>/", ResultDetailView.as_view(), name="result_detail"),
]
