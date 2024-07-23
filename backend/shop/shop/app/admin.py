from django.contrib import admin
from django.utils.html import format_html
from app.models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ('title',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # Дополнительные настройки поиска
        return queryset, use_distinct
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)