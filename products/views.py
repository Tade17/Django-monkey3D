from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    model= Product
    template_name='products/product_list.html'
    context_object_name='product_list'
    queryset=Product.objects.filter(available=True)

class ProductDetailView(DetailView):
    model=Product
    template_name='products/product_detail.html'   