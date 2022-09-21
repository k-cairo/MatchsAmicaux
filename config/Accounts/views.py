from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "club", "category", "practice_level", "region")
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Email",
            "club": "Club",
            "category": "Catégorie",
            "practice_level": "Niveau de Pratique",
            "region": "Région"
        }


def signup(request):
    context = {}

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('Website-index')
        else:
            context["errors"] = form.errors

    form = CustomSignupForm()
    context["form"] = form

    return render(request, "Accounts/signup.html", context=context)

