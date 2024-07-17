
from django.core.cache import cache
from .models import ProductCategory

def cache_product_categories():
    categories = list(ProductCategory.objects.values_list('name', flat=True))
    cache.set('product_categories', categories, timeout=None)  # None ��������, ��� ��� �� �������

# �������� ��� �������, ����� ��������� ��� ��� ������ ���������� ��� � ������ ������
cache_product_categories()