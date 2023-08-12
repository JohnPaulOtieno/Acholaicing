from django.views.generic.base import TemplateView

class OffersView(TemplateView):
    template_name = "offers/offers.html"

    def cake_offers(request):
        cakes = Cake.objects.all()
        return render(request, 'offers/offers.html', {'cakes': cakes})


#viewing the Cake form 

from django.shortcuts import render
from .models import Cake

def cake_offers(request):
    cakes = Cake.objects.all()
    return render(request, 'offers/offers.html', {'cakes': cakes})
    