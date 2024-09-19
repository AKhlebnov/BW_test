from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-панель для управления продуктами.
    """

    list_display = ('name', 'description')
    search_fields = ('name',)
