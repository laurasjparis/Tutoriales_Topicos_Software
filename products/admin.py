from django.contrib import admin
from .models import Product, Comment

# Registramos los modelos para que aparezcan en el panel de administración
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_at')
