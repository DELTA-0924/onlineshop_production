
from django.core.cache import cache
from .models import ProductCategory

def cache_product_categories():
    categories = list(ProductCategory.objects.values_list('name', flat=True))
    cache.set('product_categories', categories, timeout=None)  # None означает, что кэш не истечет

# Вызовите эту функцию, чтобы заполнить кэш при старте приложения или в нужный момент
cache_product_categories()