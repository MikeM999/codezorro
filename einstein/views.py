from django.views import View
from einstein.models import Language, Topic, Narrative
from einstein.models import Xmail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LanguageForm, XmailForm


def get_code(request):
    text = ""
    form = LanguageForm()
    if request.method == 'POST':
        form = LanguageForm(request.POST, request.FILES)
        if form.is_valid():
            language = form.cleaned_data['language']
            topic = form.cleaned_data['topic']
            try:
                querySet = Language.objects.filter(
                    name=language).values('code')
                languageCode = querySet[0]['code']
                querySet = Topic.objects.filter(
                    name=topic).values('code')
                topicCode = querySet[0]['code']
                if topicCode == "24":
                    querySet = Narrative.objects.filter(
                        code="SQL").values('text')
                    text = querySet[0]['text']
                else:
                    narrativeCode = languageCode + topicCode

                    querySet = Narrative.objects.filter(
                        code=narrativeCode).values('text')
                    text = querySet[0]['text']
            # End of try block
            except:
                text = 'The selected topic "' + str(topic) + \
                    '" is not relevant to the ' + \
                    str(language) + " programming language."
            # End of except block
        # End of if form.is_valid()
    # End of if request.method == "POST"

    context = {'text': text, 'form': form}
    return render(request, 'einstein/language.html', context)


def createEmail(request):
    form = XmailForm()
    if request.method == 'POST':
        form = XmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('thankyou')

    context = {'form': form}
    return render(request, "einstein/contact.html", context)


def donate(request):
    return render(request, 'einstein/donate.html')


def about(request):
    return render(request, 'einstein/about.html')


def thankyou(request):
    return render(request, 'einstein/thankyou.html')
