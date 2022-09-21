from django import forms
from django.forms import Textarea

from Website.models import Announce, Comment


class DateInput(forms.DateInput):
    input_type = 'date'


class PostAnnounceForm(forms.ModelForm):
    class Meta:
        model = Announce
        fields = ["date", "location", "hour", "desired_level"]
        labels = {
            "date": "Date",
            "location": "Lieu",
            "hour":  "Coup d'envoi",
            "desired_level": "Catégorie & Niveau Souhaité"
        }
        widgets = {
            "date": DateInput()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            'body': Textarea(attrs={'cols': 40, "rows": 5, "placeholder": "Votre Commentaire ..."}),
        }
        labels = {"body": ""}
