def transition():
    word = input("Enter the Word : ")
    
    print("Protal transition activated!")
    
    magic_bag = ["staff","potion","spellbook"]
    
    old = magic_bag.pop(0)
    print(f"Ejected oldest item: {old}")
    magic_bag.append(word.strip())
    
    print(f"Current items in the magic bag: {magic_bag}")
    

transition()

    