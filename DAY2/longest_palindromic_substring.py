def main():
    str1 = input("Enter the String : ")
    longest = ''
    
    for i in range(len(str1)):
        for j in range(i+1, len(str1) +1):
            sub = str1[i:j]
            if sub == sub[::-1]:
                if len(sub) > len(longest):
                    longest = sub
    print(f'Longest Substring is - {longest}')

main()