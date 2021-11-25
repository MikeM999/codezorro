from django.views import View
from einstein.models import Language, Topic, Narrative
from einstein.models import Xmail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import LanguageForm, XmailForm
from django.conf import settings
from django.urls import reverse


import stripe


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
                if topicCode == "24" and languageCode != "JS":
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
                    '" is not supported by the ' + \
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
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1JjOP9EmU9UV2DyjtnmxEWl8',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('donatethankyou')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('get_code')),
    )
    context = {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'einstein/donate.html', context)


def about(request):
    return render(request, 'einstein/about.html')


def thankyou(request):
    return render(request, 'einstein/thankyou.html')


def jsnotes(request):
    return render(request, 'einstein/jsnotes.html')


def donatethankyou(request):
    return render(request, 'einstein/donatethankyou.html')
