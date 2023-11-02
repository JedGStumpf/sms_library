from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from .models import ValidEmail
from .forms import (
    SignInForm,
    NonAdminCustomUserCreationForm,
)


class CustomSignInView(LoginView):
    form_class = SignInForm


@login_required
def sign_out(request):
    logout(request)
    messages.info(request, "Signed out successfully")
    return redirect("sign_in")


def signup(request):
    """Custom Sign Up View

    Checks if the Form is a POST method, 
    then checks if the form is valid,
    finally checks if the requeting user's email is in
        The ValidEmail list stored in the DB
        
    Returns:
        New User Account
    """
    if request.method == "POST":
        form = NonAdminCustomUserCreationForm(request.POST)

        if form.is_valid():
            form_email = form.cleaned_data["email"]
            valid_email = ValidEmail.objects.filter(email=form_email).exists()

            if valid_email:
                user = form.save()
                raw_password = form.cleaned_data.get("password1")
                grade = form.cleaned_data.get("grade")
                user = authenticate(
                    request, email=user.email, grade=grade, password=raw_password
                )

                # if user is not None:
                #     login(request, user)
                # else:
                if user is None:
                    messages.error(request, "User is Not Authorized")

                return redirect("library:home")
            else:
                messages.error(
                    request, "The Email Provided Is Not Approved For An Account"
                )
                form = NonAdminCustomUserCreationForm()

    else:

        form = NonAdminCustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """Custom Reset Password View
    See stms_library URLS

    Sends email to requesting user.
    django backend already implements a check to see
        if the requesting email exists in current users
        and will not send an email if it does not
    """

    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly."
        " If you don't receive an email, "
        "please make sure you've entered the address you registered with, and check your spam folder."
    )
    success_url = reverse_lazy("users:sign_in")
