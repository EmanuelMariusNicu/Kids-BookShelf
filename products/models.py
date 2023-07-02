from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=80)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """
        Ensure correct plural of Category
        in admin UI
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Parent class for all products
    of different types
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE)
    books = models.CharField(max_length=80)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.books