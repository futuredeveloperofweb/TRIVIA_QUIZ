from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("quiz/", include("apps.quiz.urls", namespace="quiz")),
    path("authentication/", include("apps.authentication.urls", namespace="authentication")),
    path('', views.home, name='home'),
]
