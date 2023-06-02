from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')

class ProductView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')

class ShopView(View):
    def get(self, request):
        return render(request, 'store/shop.html')