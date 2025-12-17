# Distributed System Simulation with Django (Multi-DB + Threads)

This project simulates a distributed system where different data types are stored in separate SQLite databases and inserted concurrently using threads, as required in the assignment.

---

## Features

- Multiple SQLite databases
- Django database routing
- Concurrent insertions using threading
- Application-level validation
- Single command execution
- Clean Django architecture

---

## Validation Rules (Application Level)

- User email must contain `@`
- Product price must be ≥ 0
- Order quantity must be > 0
- No database-level validation is used

---

## Setup Instructions

### Install Dependencies
```bash
pip install django

python manage.py makemigrations core

python manage.py migrate --database=users_db
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db

python manage.py run_inserts

```

---

### Output
```bash
PS C:\Users\ACER\Desktop\Projects\tradexa_assignment> python manage.py run_inserts
Product failed: (10, 'Earbuds', -50.0) | Negative price not allowed
Order failed: (8, 8, 8, 0) | Invalid quantity
Order failed: (9, 9, 1, -1) | Invalid quantity
User inserted: David
Product inserted: Laptop
Order inserted: user=1, product=1
User inserted: Jane
Product inserted: Laptop
Order inserted: user=2, product=2
User inserted: Bob
Product inserted: Smartwatch
Order inserted: user=3, product=3
Order inserted: user=6, product=6
User inserted: Frank
Product inserted: Smartphone
Order inserted: user=4, product=4
User inserted: Alice
User inserted: Alice
Order inserted: user=7, product=7
Product inserted: Gaming Chair
User inserted: Henry
Order inserted: user=5, product=5
Product inserted: Keyboard
User inserted: Eve
Order inserted: user=10, product=11
User inserted: Charlie
Product inserted: Monitor
User inserted: Grace
Product inserted: Mouse
Product inserted: Headphones
All insertions completed

```

⚠️ Note: Output order may vary due to concurrent thread execution.

