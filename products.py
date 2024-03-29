import uuid


class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


class Warehouse:

    def __init__(self):
        self.products = []
        
    def add_product(self, product_name, price):
        tab = []
        for prod in self.products:
            tab.append(prod.product_name)
        
        if product_name not in tab:
            self.products.append(Product(product_name, price))
        
        
        
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Mobile Phone', 1990.0)
print(warehouse.products)

