import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_practise_1.settings')

django.setup()


from store.models import Category, Product

if __name__ == "__main__":

    obj = Product.objects.create(name='Bell Pepper',
                             description='болгарский перец',
                             price=120,
                             image='static/products/product-1.jpg',
                             category=Category.objects.get(name='Vegetables'))
    obj = Product.objects.create(name='Strawberry',
                                 description='клубника',
                                 price=120,
                                 image='static/products/product-2.jpg',
                                 category=Category.objects.get(name='Fruits'))
    obj = Product.objects.create(name='Green Beans',
                                 description='горошек',
                                 price=120,
                                 image='static/products/product-3.jpg',
                                 category=Category.objects.get(name='Vegetables'))
    obj = Product.objects.create(name='Purple Cabbage',
                                 description='краснокочанная капуста',
                                 price=120,
                                 image='static/products/product-4.jpg',
                                 category=Category.objects.get(name='Vegetables'))
    obj = Product.objects.create(name='Tomatoe',
                                 description='томат',
                                 price=120,
                                 image='static/products/product-5.jpg',
                                 category=Category.objects.get(name='Vegetables'))
    obj = Product.objects.create(name='Brocolli',
                                 description='брокколи',
                                 price=120,
                                 image='static/products/product-6.jpg',
                                 category=Category.objects.get(name='Vegetables'))