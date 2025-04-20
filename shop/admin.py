from django.contrib import admin
import nested_admin

from .models import Category, SubCategory, Product, ProductVariant, ProductVariantImage


class ProductVariantImageInline(nested_admin.NestedTabularInline):
    model = ProductVariantImage
    extra = 1


class ProductVariantInline(nested_admin.NestedStackedInline):
    model = ProductVariant
    extra = 1
    inlines = [ProductVariantImageInline]


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    list_display = ["name", "subcategory"]
    inlines = [ProductVariantInline]


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 1
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name", )}
    inlines = [SubCategoryInline]
