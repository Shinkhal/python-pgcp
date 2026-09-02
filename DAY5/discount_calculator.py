
def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05,discount=0.0,delivery_fee=0.0):
    subtotal = base_price + sum(items)
    discounted = subtotal * ( 1 - discount/100)
    tax_value = discounted * tax_rate
    final_bill = tax_value + delivery_fee + discounted
    
    return round(final_bill,2)

total1 = calculate_cafeteria_bill(100.0)
print(f'{total1:.2f}')

total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08,discount=10.0, delivery_fee=15.0)
print(f'{total2:.2f}')