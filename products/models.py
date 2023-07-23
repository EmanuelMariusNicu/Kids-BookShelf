from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    
    class Meta:
        """
        Ensure correct plural of Category
        in admin UI
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __str__(self):
        return self.friendly_name

class Product(models.Model):
    """
    Parent class for all products
    of different types
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE)
    sku = models.CharField(max_length=80,  null=True, blank=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name