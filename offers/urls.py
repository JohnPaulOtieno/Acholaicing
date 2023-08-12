from django.urls import path

from offers.views import OffersView
from . import views

urlpatterns = [
    path("", OffersView.as_view(), name="offers"),
    path("", views.cake_offers, name='cake_offers'),
]