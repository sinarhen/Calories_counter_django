from django.db import models
import os


# Create your models here.
def create_path(instance, filename):
    return os.path.join(
        instance.name,
        filename
    )


class Product(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255, blank=False)
    price = models.DecimalField(verbose_name="Average Price", blank=False, decimal_places=1)
    calories = models.IntegerField(verbose_name="Calories", blank=False)
    protein = models.DecimalField(verbose_name="Protein", max_digits=4, decimal_places=1, default=0.0)
    carbohydrate = models.DecimalField(verbose_name="Carbohydrate", max_digits=4, decimal_places=1, default=0.0)
    fats = models.DecimalField(verbose_name="Fats", decimal_places=1, max_digits=4, default=0.0)
    photo = models.ImageField(verbose_name='Photo', db_index=True, max_digits=4, upload_to=create_path)
    type_of_food = models.ForeignKey('FoodType', max_digits=4, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FoodType'
        verbose_name_plural = 'FoodTypes'
        ordering = (id,)


class FoodType(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FoodType'
        verbose_name_plural = 'FoodTypes'
        ordering = (id,)
