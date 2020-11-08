from .models import DigiKalaProduct, ChangeLogProduct
from django.contrib import admin


admin.site.register(ChangeLogProduct)

@admin.register(DigiKalaProduct)
class DigiKalaProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']