
from django import forms
from .models import Language, Topic


class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(
        queryset=Language.objects.all().order_by('name'), label="Pick a Language")
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all().order_by('name'), label="Select a Topic")


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
