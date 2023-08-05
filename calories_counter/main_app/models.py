from django.db import models
import os

def path_for_type(instance, filename):
    """
    Function for generating file path based on the instance and filename.
    
    Args:
        instance: The instance of the model.
        filename: The name of the file.
    
    Returns:
        The file path for the given instance and filename.
    """
    return os.path.join(
        f"Foodtypes/{instance.name}" if isinstance(instance, FoodType) else f"Foodtypes/{instance.type_of_food.name}/",
        f"{instance.name}",
        filename
    )

class Product(models.Model):
    """
    Model representing a product.
    """

    name = models.CharField(verbose_name="Name", max_length=255, blank=False)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name="Average Price", blank=False, max_digits=10, decimal_places=1)
    calories = models.IntegerField(verbose_name="Calories", blank=False)
    protein = models.DecimalField(verbose_name="Protein", max_digits=4, decimal_places=1, default=0.0)
    carbohydrate = models.DecimalField(verbose_name="Carbohydrate", max_digits=4, decimal_places=1, default=0.0)
    fats = models.DecimalField(verbose_name="Fats", decimal_places=1, max_digits=4, default=0.0)
    photo = models.ImageField(verbose_name='Photo', upload_to=path_for_type)
    type_of_food = models.ForeignKey('FoodType', on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        """
        Returns the string representation of the product.
        """
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ("id",)

    def get_absolute_url(self):
        """
        Returns the absolute URL of the product.
        """
        return f"/catalog/{self.type_of_food_id}/{self.id}/"

class FoodType(models.Model):
    """
    Model representing a food type.
    """

    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(verbose_name='Photo', upload_to=path_for_type, blank=True)

    def __str__(self):
        """
        Returns the string representation of the food type.
        """
        return self.name

    class Meta:
        verbose_name = 'FoodType'
        verbose_name_plural = 'FoodTypes'
        ordering = ("id",)
