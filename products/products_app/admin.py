from django.contrib import admin
from products_app.models import Products


# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'cost', 'remainder']
    list_filter = ['name']
    search_fields = ['category', 'cost']
    fields = ['id', 'name', 'text', 'category', 'remainder', 'cost']
    readonly_fields = ['id']


admin.site.register(Products, ProductsAdmin)

