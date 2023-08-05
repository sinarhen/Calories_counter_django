# Calories Counter With Django
This project provides calories counter website with Django Framework 

## Example of usage
Start the project with runserver command:

```cmd
py manage.py runserver
```

## Home page

After starting the project and open http://localhost:8000 we see the next page

![image](https://github.com/sinarhen/Calories_counter_django/assets/105736826/5818ddc6-362d-4ef7-8562-2c672bc0d549)

## Categories Page

After clicking on Catalog button on the Home page 
it redirects us to the page http://localhost:8000/catalog/ with the following content:

![image](https://github.com/sinarhen/Calories_counter_django/assets/105736826/5f144874-b517-411c-9068-b0fb74fdd6fc)

### Category Model 
categories represented by model FoodType with the following fields: 
```python
class FoodType(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(verbose_name='Photo', upload_to=path_for_type, blank=True)
```

## Products Page

Each Product model is binded with the FoodType model with relation type "ManyToOne" where "Many" is products and "One" is category

After picking the category it redirects us to http://127.0.0.1:8000/catalog/<int:category_pk>/

### Product Model

```python
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
```

## Single Product Page

After picking a product and clicking on it it redirects us to http://127.0.0.1:8000/catalog/<int:category_pk>/<int:product_pk>/ and we see the following page:

![image](https://github.com/sinarhen/Calories_counter_django/assets/105736826/b356cadb-8b57-47fd-8a9e-bc03ff1148c0)

## Cart 

After choosing an quantity of product and clicking "Add to diet" button it redirects us to http://127.0.0.1:8000/cart/ with the following content:

![image](https://github.com/sinarhen/Calories_counter_django/assets/105736826/b96ac135-c100-4070-81f8-ce4f683e5dbc)

### Cart functionality 

Each product added to cart is saved into session attributes which is not the best solution generally, but in django it's the best option to do release this functionality

#### Table

Table of added products is a simple html table with the values pasted with jinja and remove button for removing the product from cart.

#### Calories calculator 

The calculator has the following view:

![image](https://github.com/sinarhen/Calories_counter_django/assets/105736826/af250f4d-080d-4e41-9b7c-bd3a4d20ebdb)



