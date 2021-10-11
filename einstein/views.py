from einstein.models import Language, Topic, Narrative
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import LanguageForm
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import pdb


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


def importData(request):
    with open('templates/narrativeData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            vCode = row[0]+row[1]
            _, created = Narrative.objects.get_or_create(
                code=vCode,
                text=row[2]
            )
            print(row[0], row[1], row[2])
        return render(request, 'einstein/language.html')


def donate(request):
    return render(request, 'einstein/donate.html')


def about(request):
    return render(request, 'einstein/about.html')


def contact(request):
    return render(request, 'einstein/contact.html')
