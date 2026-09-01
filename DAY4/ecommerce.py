catalog = {"P01": {"price": 100.0, "stock": 5},"P02": {"price": 50.0, "stock": 2}}

class ProductNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    pass

def process_order(catalog, order):
    for product_id in order :
        if product_id not in catalog:
            raise ProductNotFoundError(
                f"Product {product_id} Not found in store catalog"
            )
            
    for product_id , quantity in order.items():
        available = catalog[product_id]["stock"]
        if quantity > available:
            raise OutOfStockError(f"Product {product_id} is out of stock. Requested: {quantity}, Available: {available}")
        
    total_price = 0.0
    for product_id, quantity in order.items():
        get_price = catalog[product_id]["price"]
        
        total_price += (get_price * quantity)
        
        catalog[product_id]["stock"] -= quantity
        
    return total_price


cart = process_order(catalog, {"P01": 2, "P02": 1})
print(cart)
print(catalog)

    