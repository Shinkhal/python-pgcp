def odd_even():
    num = int(input("Enter the Number : "))

    if num % 2 ==0 :
        print(f'{num} is an Even Number')
    else:
        print(f'{num} is an Odd Number')

print("="*50)
odd_even()