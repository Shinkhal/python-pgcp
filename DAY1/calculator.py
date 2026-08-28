def calc():
    n1 = int(input("Enter Number 1 : "))
    n2 = int(input("Enter Number 2 : "))
    op = input("Enter Operation : ")

    if op == '+':
        print(f'Result : {n1 + n2}')
    elif op == '-':
        print(f'Result : {n1 - n2}')
    elif op == '*':
        print(f'Result : {n1 * n2}')
    elif op == '/':
        print(f'Result : {n1 - n2}')
    else :
        print("Invalid Operation , try again")


calc()