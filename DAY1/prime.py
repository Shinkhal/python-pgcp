def prime():
    n = int(input("Enter the Number : "))

    limit = n//2
    d =2
    while d <= limit:
        if ( n % d ==0):
            break
        d+=1
    else:
        print(f'{n} is a Prime Number')


prime()