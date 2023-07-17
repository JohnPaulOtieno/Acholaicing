from django.urls import path

from offers.views import OffersView


urlpatterns = [
    path("", OffersView.as_view(), name="offers"),
]