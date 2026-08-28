"""
Exercise 6: Sum of N Natural Numbers
Write a script that accepts a positive integer 
N
 from the user and calculates the sum of all natural numbers up to 
N
Sample Input: N = 10
Sample Output: Sum: 55


"""

def sum():
    n = int(input("Enter the Number : "))

    sum = (n*(n+1))//2
    print(f'Sum : {sum}')


sum()