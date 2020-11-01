from django.urls import path, include

from .views import (
    product_list_view,

    product_detail_view,
    product_create_view,
    product_delete_view,
)
app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),

]
