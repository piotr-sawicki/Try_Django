from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

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


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    print('id: ', id)
    for p in Product.objects.all():
        print(p.id, p.title, p.price, sep=' - ')
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'products/product_list.html', context)