from django.http import HttpResponse
from django.shortcuts import render

from Accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "club", "region")


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        club = request.POST.get("club")
        region = request.POST.get("region")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "Accounts/signup.html",
                          context={"error": "Les mots de passes ne sont pas identiques."})

        # TODO
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Bienvenue !")
        else:
            contex['errors'] = form.errors

    form = CustomSignupForm()
    contex["form"] = form

    return render(request, "Accounts/signup.html", context=contex)
