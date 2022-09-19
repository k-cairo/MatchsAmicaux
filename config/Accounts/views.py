from django.http import HttpResponse
from django.shortcuts import render

from Accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "club", "region")
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Email",
            "club": "Club",
            "region": "Région"
        }


def signup(request):
    context = {}

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Bienvenue")
        else:
            context["errors"] = form.errors

    form = CustomSignupForm()
    context["form"] = form

    return render(request, "Accounts/signup.html", context=context)
