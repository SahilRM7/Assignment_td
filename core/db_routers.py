class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model.__name__ == 'User':
            return 'users_db'
        if model.__name__ == 'Product':
            return 'products_db'
        if model.__name__ == 'Order':
            return 'orders_db'
        return None

    def db_for_write(self, model, **hints):
        if model.__name__ == 'User':
            return 'users_db'
        if model.__name__ == 'Product':
            return 'products_db'
        if model.__name__ == 'Order':
            return 'orders_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'user':
            return db == 'users_db'
        if model_name == 'product':
            return db == 'products_db'
        if model_name == 'order':
            return db == 'orders_db'
        return None
