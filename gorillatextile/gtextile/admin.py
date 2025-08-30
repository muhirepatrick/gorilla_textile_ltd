from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_type", "is_active")
    search_fields = ("username", "email")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "created_by", "created_at")
    list_filter = ("category", "created_by")
    search_fields = ("name", "description")

admin.site.register(ProductImage)