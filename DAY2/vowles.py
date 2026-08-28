def count():
    str1 = input("Enter your sentence : ")
    
    vowels = ['a','e','i','o','u']
    print("Vowels Frequencies: ")
    for vowel in vowels:
        print(f'{vowel}: {str1.count(vowel)}')
        
    consonant = 0
    for c in str1:
        if c.isalpha() and c not in vowels:
            consonant += 1
    
    print(f"Total Consonants : {consonant}")
    
    
count()
    