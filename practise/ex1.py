products = [
    {"id":1,"name":"Laptop","category":"Electronics","price":55000,"quantity":10},
    {"id":2,"name":"Chair","category":"Furniture","price":1500,"quantity":50}
]

id_count = len(products)

def welcome():
    print('-'*50)
    print("Welcome to Product Inventory Management System")
    print(f'1. Add Products \n 2. View all Products \n 3. Search Products \n 4. Update Product \n 5. Delete Product \n 6. Exit')
    print("-"*50)

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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _ :
                print("Invalid Try Again...")




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


def view_products():
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}')
    print('-'*60)
    for product in products:
        pid,name,category,price,quantity = product.values()

        print(f'{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    print('-'*60)


if __name__ ==  '__main__' :
    main()