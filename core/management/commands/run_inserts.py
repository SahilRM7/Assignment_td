from django.core.management.base import BaseCommand
from core.models import User, Product, Order
import threading

USERS_DATA = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", "bob@example.com"),
    (3, "Charlie", "charlie@example.com"),
    (4, "David", "david@example.com"),
    (5, "Eve", "eve@example.com"),
    (6, "Frank", "frank@example.com"),
    (7, "Grace", "grace@example.com"),
    (8, "Alice", "alice@example.com"),
    (9, "Henry", "henry@example.com"),
    (10, "Jane", "jane@example.com"),
]

PRODUCTS_DATA = [
    (1, "Laptop", 1000.00),
    (2, "Smartphone", 700.00),
    (3, "Headphones", 150.00),
    (4, "Monitor", 300.00),
    (5, "Keyboard", 50.00),
    (6, "Mouse", 30.00),
    (7, "Laptop", 1000.00),
    (8, "Smartwatch", 250.00),
    (9, "Gaming Chair", 500.00),
    (10, "Earbuds", -50.00),
]

ORDERS_DATA = [
    (1, 1, 1, 2),
    (2, 2, 2, 1),
    (3, 3, 3, 5),
    (4, 4, 4, 1),
    (5, 5, 5, 3),
    (6, 6, 6, 4),
    (7, 7, 7, 2),
    (8, 8, 8, 0),
    (9, 9, 1, -1),
    (10, 10, 11, 2),
]


class Command(BaseCommand):
    help = "Run concurrent inserts for Users, Products, Orders"

    def handle(self, *args, **kwargs):
        threads = []

        for data in USERS_DATA:
            t = threading.Thread(target=self.insert_user, args=(data,))
            threads.append(t)

        for data in PRODUCTS_DATA:
            t = threading.Thread(target=self.insert_product, args=(data,))
            threads.append(t)

        for data in ORDERS_DATA:
            t = threading.Thread(target=self.insert_order, args=(data,))
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        self.stdout.write(self.style.SUCCESS("All insertions completed"))

    def insert_user(self, data):
        try:
            _, name, email = data
            if not name or "@" not in email:
                raise ValueError("Invalid user data")
            User.objects.using('users_db').create(name=name, email=email)
            print(f"User inserted: {name}")
        except Exception as e:
            print(f"User failed: {data} | {e}")

    def insert_product(self, data):
        try:
            _, name, price = data
            if price < 0:
                raise ValueError("Negative price not allowed")
            Product.objects.using('products_db').create(name=name, price=price)
            print(f"Product inserted: {name}")
        except Exception as e:
            print(f"Product failed: {data} | {e}")

    def insert_order(self, data):
        try:
            _, user_id, product_id, quantity = data
            if quantity <= 0:
                raise ValueError("Invalid quantity")
            Order.objects.using('orders_db').create(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity
            )
            print(f"Order inserted: user={user_id}, product={product_id}")
        except Exception as e:
            print(f"Order failed: {data} | {e}")
