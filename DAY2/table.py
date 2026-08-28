def table_generator():
    num = int(input("Enter the Number : "))

    for i in range(1,10+1):
        print(f'{num} x {i} = {num * i}')

table_generator()