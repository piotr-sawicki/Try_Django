"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import pages.views as pages_v
import products.views as products_v

urlpatterns = [
    path('', pages_v.home_view, name='home'),
    path('contact/', pages_v.contact_view),
    path('products/', products_v.product_list_view),
    path('product/<int:id>/', products_v.dynamic_product_detail_view),
    path('create_product/', products_v.product_create_view),
    path('delete_product/<int:id>/', products_v.product_delete_object_view),
    path('about/', pages_v.about_view),
    path('admin/', admin.site.urls),
]
