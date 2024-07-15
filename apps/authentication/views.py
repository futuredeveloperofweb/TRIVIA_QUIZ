from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.conf import settings
import logging

# Initialize logger
logger = logging.getLogger(__name__)


def register_view(request):
    """Handle user registration."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f"User registered and logged in: {user.username}")
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    """Handle user login."""
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User logged in: {user.username}")
            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    """Handle user logout."""
    logout(request)
    logger.info("User logged out")
    return redirect("home")


def password_reset_view(request):
    """Handle password reset."""
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                token_generator=default_token_generator,
                from_email=settings.DEFAULT_FROM_EMAIL,
                email_template_name="registration/password_reset_email.html",
            )
            logger.info("Password reset email sent")
            return redirect("password_reset_done")
    else:
        form = PasswordResetForm()
    return render(request, "registration/password_reset_form.html", {"form": form})
