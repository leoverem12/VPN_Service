from django import forms

from .models import Subscription


class SubForm(forms.ModelForm):
    sub = forms.ChoiceField(
        choices=Subscription,
        label="Вибріть підпискау",
        attrs=forms.Select(attrs={"class": "form-control"}),
        )