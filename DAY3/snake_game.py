def snake_game():
    
    grid = [['.']*5 for _ in range(5)]
    
    grid[2][3] = "F"
    
    row = int(input("Enter row :"))
    column = int(input("Enter column :"))
    
    grid[row][column] = "S"
    
    if row == 2 and column == 3 :
        grid[2][3] = "S"
        print("Yum! sake ate the food!")
    
    for row in grid:
        print(*row)
    
    
snake_game()