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
    list_display = ["name", "subcategory", "is_featured", "display_variant_count"]
    list_editable = ["is_featured"]
    search_fields = ["name", "description"]
    autocomplete_fields = ["subcategory"]
    prepopulated_fields = {"slug": ("name", )}
    actions = ["mark_as_featured"]
    inlines = [ProductVariantInline]
    
    def display_variant_count(self, obj):
        return obj.variants.count()
    display_variant_count.short_description = "Nombre de variantes"
    
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f"{updated} produits ont été marqués comme mis en avant")
    mark_as_featured.shot_description = "Marquer comme mis en avant"


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 1
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name", )}
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

