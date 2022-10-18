from django.conf import settings
from main_app.models import Product


class Cart:

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = item['price'] * item['quantity']
            item['total_calories'] = item['product'].calories * item['quantity']
            item['total_protein'] = item['product'].protein * item['quantity']
            item['total_carbohydrate'] = item['product'].carbohydrate * item['quantity']
            item['total_fats'] = item['product'].fats * item['quantity']
            yield item
        print(self.cart)

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': float(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product, quantity=0, update_quantity=False):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if quantity >= self.cart[product_id]['quantity']:
            del self.cart[product_id]

        # if product_id not in self.cart:
        #     self.cart[product_id] = {'quantity': 0,
        #                              'price': float(product.price)}
        else:
            self.cart[product_id]['quantity'] -= quantity
        self.save()

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def get_total_calories(self):
        return sum(item['product'].calories * item['quantity'] for item in self.cart.values())

    def get_total_protein(self):
        return sum(item['product'].protein * item['quantity'] for item in self.cart.values())

    def get_total_carbohydrate(self):
        return sum(item['product'].carbohydrate * item['quantity'] for item in self.cart.values())

    def get_total_fats(self):
        return sum(item['product'].fats * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
