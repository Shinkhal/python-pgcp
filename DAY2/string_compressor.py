def compressor():
    sen = input("Enter the String : ")
    
    if sen == '':
        return
    count = 1
    
    new_str =''
    for i in range(1, len(sen)):
        if sen[i] == sen[i-1]:
            count+=1
        else:
            new_str += sen[i-1] + str(count)
            count = 1
            
    new_str += sen[-1] + str(count)
   
    if len(new_str) < len(sen): 
        print(new_str)
    else:
        print(sen)
        
        
compressor()
            