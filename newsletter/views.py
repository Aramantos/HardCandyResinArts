from django.shortcuts import render

# Create your views here.

def newsletter(request):
    """ A view to return the about page """

    return render(request, 'newsletter/newletter.html')