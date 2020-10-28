from django.shortcuts import render

from .models import Product
# Create your views here.
def product_detail_view(request):
    context = {
        'object': Product.objects.get(id=1),
    }
    return render(request, "products/product_detail.html", context)