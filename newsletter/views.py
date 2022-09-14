from django.shortcuts import render

from django.template import loader
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def newsletter(request):
    """ A view to return the newsletter page """

    return render(request, 'newsletter/newsletter.html')

# def send_mail(request):
    
