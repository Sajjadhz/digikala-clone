from django.contrib import admin
from .models import Product, DigiKalaProducts
# Register your models here.
admin.site.register(Product)
@admin.register(DigiKalaProducts)
class DigiKalaProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']