from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ProductBySearhView, ProductViewSet,ProductByCategoryView,ProductCategoryViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', ProductCategoryViewSet, basename='product-category')
urlpatterns = [
    path('', include(router.urls)),
    path('category/', ProductByCategoryView.as_view(), name='product-by-category'),
    path('product-search/', ProductBySearhView.as_view(), name='product-by-search')
]

