from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product


# Create your views here.
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)
#

# def product_create_view(request):
#     if request.method == 'POST':
#         my_title = request.POST.get('title')
#         print(my_title)
#         # Product.objects.create(title=my_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



def product_detail_view(request):
    context = {
        'object': Product.objects.get(id=1),
    }
    return render(request, "products/product_detail.html", context)


def dynamic_product_detail_view(request, id):
    context = {
        'object': Product.objects.get(id=id),
    }
    return render(request, "products/product_detail.html", context)
