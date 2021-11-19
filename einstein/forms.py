from django import forms
from django.forms.models import ModelForm
from .models import Language, Topic, Xmail


class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(
        queryset=Language.objects.all().order_by('name'), label="Pick a Language:")
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all().order_by('name'), label="Select a Topic:")


class XmailForm(ModelForm):
    class Meta:
        model = Xmail
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'rows': 10, 'cols': 70}),
        }
