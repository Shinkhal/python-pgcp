class InvalidPhoneNumberError(Exception):
    pass


contacts = {}


def check(name):
    if name == '' or not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    return True


def check_phone(phone):
    try:
        int(phone)
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")
    return True


def register_contact(phonebook, name, phone_input):
    check(name)
    check_phone(phone_input)

    phonebook[name] = phone_input

    return phonebook

contacts = register_contact(contacts, "Alice", "0987654321")
print(contacts)

try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e)