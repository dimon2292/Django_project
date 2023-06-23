import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_practise_1.settings')

django.setup()


from store.models import Category, Product

if __name__ == "__main__":
    obj = Product.objects.create(name='Chilli',
                                 description='перец чили',
                                 price=120,
                                 image='static/products/product-12.jpg',
                                 category=Category.objects.get(name='Vegetables'))