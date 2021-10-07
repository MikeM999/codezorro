
from django import forms
from .models import Language, Topic


class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset=Language.objects.all().order_by('name'), label="Select a language")
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all().order_by('name'), label="Select a topic")
=======
        queryset=Language.objects.all().order_by('name'), label="Language")
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all().order_by('name'), label="Topic")
>>>>>>> 2d134f0 (07102021-1)
