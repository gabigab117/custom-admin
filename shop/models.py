from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Catégorie"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    class Meta:
        verbose_name = "Sous-catégorie"


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False, verbose_name="Promo")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Produit"


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color}"
    
    class Meta:
        verbose_name = "Produit variant"


class ProductVariantImage(models.Model):
    variant = models.ForeignKey(ProductVariant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image of {self.variant}"
    
    class Meta:
        verbose_name = "Image de produit variant"
