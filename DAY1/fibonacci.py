def main():
    n = int(input("Enter the number : "))

    a,b = 0,1
    for _ in range (n):
        print(a, end =',')
        a,b = b,a+b


print('=' * 80)

main()