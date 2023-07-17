from django.views.generic.base import TemplateView

class ShopView(TemplateView):
    template_name = "shop/shop.html"