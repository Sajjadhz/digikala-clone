from .models import DigiKalaProducts
from django.contrib import admin

# Register your models here.
@admin.register(DigiKalaProducts)
class DigiKalaProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']