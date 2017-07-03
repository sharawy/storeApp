from django.contrib import admin
from .models import Product,Category,Cart,Order
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','category',)
    list_display_links = ('name','category',)
    search_fields = ('name','category__name','quantity',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('total', 'status',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'total',)


