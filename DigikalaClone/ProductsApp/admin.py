from django.contrib import admin
from .models import Product, DigiKalaProducts, Stock, Store
# Register your models here.
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Store)
@admin.register(DigiKalaProducts)
class DigiKalaProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']