catalog = {"P01": {"price": 100.0, "stock": 5},"P02": {"price": 50.0, "stock": 2}}

class ProductNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    pass

def process_order(catalog, order):
    ...

