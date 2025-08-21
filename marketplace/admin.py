from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'author__username')
