def cargo_scanner():
    wagons = ["coal", "iron", "gold", "coal","timber", "coal"]
    
    resource = input("Enter the resource you want to find : ")
    
    if resource in wagons :
        count = wagons.count(resource)
        idx = wagons.index(resource)
        
        print(f"Number of {resource} wagons: {count}")
        print(f"First {resource} wagon is at index : {idx}")
    else:    
        print("Resource not found on the train!")
        
cargo_scanner()