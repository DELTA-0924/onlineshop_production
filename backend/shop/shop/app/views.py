

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets,pagination,generics
from rest_framework.response import Response
from rest_framework.views import APIView,status
from .models import Product,ProductCategory
from .serializers import ProductSerializer,ProductCategorySerializer
from django.core.cache import cache
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class CustomPagination(PageNumberPagination):
    page_size = 6  # ”кажите ваш размер страницы здесь
    page_size_query_param = 'page_size'
    max_page_size = 100  # ћаксимальный размер страницы, если это нужно
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        category_name = self.request.query_params.get('category')
        if category_name == "Main":
            return Product.objects.order_by('title')
        else:
            return Product.objects.filter(category__name=category_name).order_by('title')

class ProductBySearhView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        category_name = self.request.query_params.get('category')
        search_query = self.request.query_params.get('query')

        queryset = Product.objects.all()

        if category_name and category_name != "Main":            
            queryset = queryset.filter(category__name=category_name)

        if search_query is not None or search_query=='':
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset