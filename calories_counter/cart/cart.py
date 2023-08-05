from django.conf import settings
from main_app.models import Product

class Cart:
    """
    A class representing a shopping cart for an e-commerce application.

    Attributes:
        request: The Django request object associated with the user's session.
    """

    def __init__(self, request):
        """
        Initialize the cart.

        Args:
            request: The Django request object associated with the user's session.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Initialize an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate through items in the cart and fetch product details from the database.

        Yields:
            Dictionary containing information about each cart item.
        """
        product_ids = self.cart.keys()
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

    # ... (Continuing with method documentation)

    def __len__(self):
        """
        Get the total number of items in the cart.

        Returns:
            Total quantity of items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.

        Args:
            product: The Product object to be added to the cart.
            quantity: The quantity of the product to be added (default is 1).
            update_quantity: If True, update the quantity of an existing product (default is False).
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': float(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    # ... (Continuing with method documentation)

    def save(self):
        """
        Save the cart data to the session and mark the session as modified.
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product, quantity=0, update_quantity=False):
        """
        Remove a product from the cart or reduce its quantity.

        Args:
            product: The Product object to be removed from the cart.
            quantity: The quantity of the product to be removed (default is 0).
            update_quantity: If True, update the quantity of an existing product (default is False).
        """
        product_id = str(product.id)
        
        if quantity >= self.cart[product_id]['quantity']:
            # Remove the product from the cart if requested quantity is greater or equal
            del self.cart[product_id]
        else:
            self.cart[product_id]['quantity'] -= quantity

        self.save()


    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.

        Returns:
            Total price of all items in the cart.
        """
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def get_total_calories(self):
        """
        Calculate the total calories of all items in the cart.

        Returns:
            Total calories of all items in the cart.
        """
        return sum(item['product'].calories * item['quantity'] for item in self.cart.values())

    # ... (Continuing with method documentation)

    def clear(self):
        """
        Clear the cart by removing all items from the session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
