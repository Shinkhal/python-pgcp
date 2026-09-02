def shift_cypher():
    str1 = input("Enter the string : ")
    shift = int(input("Shift by Value : "))
    
    letters = [chr(ord(c)+ shift) for c in str1]
    res = "".join(letters)
    
    print(res)
    
  
shift_cypher()