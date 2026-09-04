products = [
    {"id":1,"name":"Laptop","category":"Electronics","price":55000,"quantity":10},
    {"id":2,"name":"Chair","category":"Furniture","price":1500,"quantity":50}
]

id_count = len(products)

def welcome():
    print('*'*60)
    print(f"{'Welcome to Product Inventory Management System':<15}")
    print('*'*60)
    print(f'1. Add Products \n2. View all Products \n3. Search Products \n4. Update Product \n5. Delete Product \n6. Exit')
    print("*"*60)

def main():
    while True:
        welcome()
        choice = int(input("Enter Your Choice : "))

        match choice:
            case 1:
                add_products()
            case 2:
                view_products()
            case 3:
                search_product()
            case 4:
                update_product()
            
            case 5:
                delete_product()
            case 6:
                break
            case _ :
                print("Invalid Try Again...")

def view_products():
    if len(products) == 0:
        print("No products in the inventory. Please add first.")
    elif len(products) == 1 :
        print_one_product(products[0])
    else:
        print_all(products)

def add_products():
    global id_count

    try:
        print('**** Add new products details ****')
        name = input("Enter Name : ").strip()
        if name == '':
            print("Name cannot be empty")
            return
        category = input("Enter Category: ")
        if category == '':
            print("Category cannot be empty")
            return
        price = int(input("Enter Price : "))
        quantity = int(input("Enter quantity : "))

        products.append(dict(id=id_count+1, name=name, category=category, price=price, quantity= quantity))

        print("Product added Successfully !")
    except:
        print("Invalid Input")


def print_all(product_list):
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}')
    print('-'*60)
    for product in product_list:
        pid,name,category,price,quantity = product.values()

        print(f'{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    print('-'*60)
    
def search_product():
    try:
        print("Enter 1 to search by ID, 2 to search by name")
        x = int(input("Enter Your choice : "))
        if x == 1:
            pid = int(input("Enter the Id to search : "))
            search_by_id(pid)
        elif x == 2:
            search_by_name()
        else:
            raise 
    except:
        print("Invalid Key")
        
        
def search_by_id(pid):
    result = [p for p in products if p['id']==pid]
    if not result:
        print(f'No product found for id {pid}')
        return None

    print_one_product(result[0])
    return result[0]

def print_one_product(p):
    pid,name,category,price,quantity = p.values()
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}')
    print('-'*60)
    print(f'{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    print('-'*60)
    
    
def search_by_name():
    name = input("Enter the name to search : ").strip()
    
    result = [p for p in products if p["name"].lower() == name.lower()]
    if not result:
        print("Product not found")
        return
    
    if len(result) == 1:
        print_one_product(result[0])
    else:
        print_all(result)
    return result

def delete_product():
    try:
        pid = int(input("Enter the ID of product to Delete : "))
        result = [p for p in products if p["id"] == pid]
        if not result:
            print("No product found")
            return 
        if len(result) == 1:
            print_one_product(result[0])
            
            choice = input("Are you sure you want to delete this Product (Y/N) : ")
            if choice.lower() ==  'y':
                products.remove(result[0])
                print("Product Deleted Successfully ...")
            else:
                return
    except:
        print("Invalid Input")            

def update_product():
    try:
        pid = int(input("Enter the ID of product to update : "))
        result = [p for p in products if p["id"]== pid]
        
        if not result:
            print("No product Found !")
            return
        else:
            name = input("Enter the New Name : ")
            category = input("Enter the new Category : ")
            price = int(input("Enter the new price : "))
            quantity = int(input("Enter the new quantity : "))
            
            result[0]["name"] = name
            result[0]["category"] = category
            result[0]["price"] = price
            result[0]["quantity"] = quantity
            
            print("Product Updated Successfuly ... ")
    except:
        print("Error Occured ...")

if __name__ ==  '__main__' :
    main()