from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings


def sign_in(request):
    if request.method == "POST":  # if the form has been submitted
        form = AuthenticationForm(request.POST)  # form bound with post data
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")

    else:
        form = AuthenticationForm()

    context = {"title": "St. Mary School Library Sign In", "form": AuthenticationForm()}

    return render(request, "library/sign_in.html", context)


# def reset_password(request):


@login_required
def sign_out(request):
    logout(request)
    messages.info(request, "Signed out successfully!")
    # context = {"title": "Sign Out"}
    return redirect("sign_in")


def home_page(request):
    context = {"title": "Library Home"}
    return render(request, "library/library_home.html", context)