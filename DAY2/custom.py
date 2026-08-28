def custom_case():
    sen = input('Enter Your Sentence : ')
    
    sen_updated = sen.lower()
    
    words = sen_updated.split(' ')
    
    sen2 = ''
    for word in words:
        new_word = word[0].upper() + word[1:]
        sen2 += new_word + " "
    
    print(sen2)
    
     
custom_case()
        