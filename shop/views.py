from django.shortcuts import render

from .models import Product


def shop(request):
    """ A view to return the shop page """

    shop = Product.objects.all()

    context = {
        'shop': shop,
    }

    return render(request, 'shop/shop.html', context)
