from django.contrib import admin

# Register your models here.
from .models import Category, Product, Discount, Cart, Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Cart)
admin.site.register(Profile)
