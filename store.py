from datetime import datetime

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_admin = False
        self.logged_in = False
        self.addresses = []
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.logged_in = True
            print(f"{self.username} logged in successfully.")
        else:
            print("Invalid username or password.")

    def logout(self):
        self.logged_in = False
        print(f"{self.username} logged out.")

    def add_address(self, address):
        self.addresses.append(address)

    def view_order_history(self):
        return self.order_history


# Product class
class Product:
    def __init__(self, name, price, description, stock):
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def increase_stock(self, quantity):
        self.stock += quantity

    def decrease_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print("Not enough stock!!")


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self,item,quantity):
        if item.stock >= quantity:
            if item.name in self.items:
                self.items[item.name]["quantity"] += quantity
            else:
                self.items[item.name] = {"product": item, "quantity": quantity}
            item.decrease_stock(quantity)
            print(f"Added {quantity} of {item.name} to your shoping cart.")
        else:
            print(f"Not enough stock for {item.name}!!")

    def remove_product(self,item):
        if item.name in self.items:
            item.increase_stock(self.items[item.name]["quantity"])
            del self.items[item.name]
            print(f"Removed {item.name} from cart.")

    def view_cart(self):
        return self.items

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total


# Order class
class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.date = datetime.now()
        self.total_price = user.shopping_cart.calculate_total()


# Admin functionalities
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_admin = True

    def add_product(self, products, name, price, description, stock):
        product = Product(name, price, description, stock)
        products[name] = product
        print(f"Product {name} added.")

    def update_product(self, product, name=None, price=None, description=None, stock=None):
        if name:
            product.name = name
        if price:
            product.price = price
        if description:
            product.description = description
        if stock is not None:
            product.increase_stock(stock - product.stock)
        print(f"Product {product.name} updated.")

    def remove_product(self, products, product):
        if product.name in products:
            del products[product.name]
            print(f"Product {product.name} removed.")


# Address class
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

