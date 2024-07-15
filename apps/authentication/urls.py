from django.urls import path
from .views import register_view, login_view, password_reset_view, logout_view

app_name = 'authentication'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('logout/', logout_view, name='logout'),
]
