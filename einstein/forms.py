
from django import forms
from .models import Language, Topic


class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(
        queryset=Language.objects.all().order_by('name'), label="Select a language")
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all().order_by('name'), label="Select a topic")
