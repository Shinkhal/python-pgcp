inventory = {"Python Basics": 10, "Learning AI": 5}

def manage_bookstore_inventory(inventory, action, book_title, qunatity =0):
    if action.lower() not in ["add", "sell", "lookup"]:
        
        print("Invalid Action ! ")
        return

    if action.lower() == "add":
        if book_title in inventory:
            inventory[book_title] += qunatity
        else:
            inventory[book_title] = qunatity
        
        return inventory
            
    if action.lower() == "sell":
        if book_title not in inventory:
            print(f'Error: Book {book_title} not in inventory')
            return
        elif inventory[book_title] < qunatity :
            print(f'Error: Insufficient Stock for {book_title}. Available: {inventory[book_title]}')
        else:
            inventory[book_title] -= qunatity
            if inventory[book_title] == 0 : del inventory[book_title]
        return inventory
    
    if action.lower() == "lookup":
        if book_title in inventory:
            return inventory[book_title]
        else:
            print("Book not found")
            return
        
    return inventory   
        
inventory = manage_bookstore_inventory(inventory, "add", "Python Advanced", 5)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science101", 1)
# inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
# inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
print(inventory)