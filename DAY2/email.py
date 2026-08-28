def email():
    
    mail = input("enter your email- ")
    
    i = mail.find("@") 
    if(i == -1):
        print("Invalid Email")
        exit(0)
        
    domain = mail[i + 1:] 
    
    print(domain)
    
email()