class InvalidPhoneNumberError(Exception):
    pass
        
contacts = {}       
def check(name):
    if name == '':
        print("Contact name must not be a non- empty string")
        return
    #char and spaces are valid
    if all(char.isalpha() or char.isspace() for char in name):
        return True
    else:
        print("Error")
    return False
        
def check_phone(phone):
    try:
        int(phone)
        print("Success")
    except:
        raise InvalidPhoneNumberError("Phone Number must contain only digits")
    
def register_contact(phonebook, name, phone_input):
    check_phone(phone_input)
    check(name)
    