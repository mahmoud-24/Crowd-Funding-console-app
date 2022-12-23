import re
def validate_name():
    first_name = input(" Please Enter your First Name :  ").lower()
    while True:
        if first_name.isalpha():
            last_name = input(" Please Enter your Last name :   ").lower()
            if last_name.isalpha():
                break
            else:
                print("Last Name Cannot Contain Spaces or Digits")
        elif first_name.isspace() or first_name.isalnum():
            print("First Name Cannot Contain Spaces or Digits")
            first_name = input(" Please Enter your First Name :  ").lower()
    return [first_name, last_name]
def validate_email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    email = input("Please Enter your E-mail :  ").lower()
    while True:
        if(re.fullmatch(regex, email)):
            break
        else:
            print("Invalid Email")
            email = input(" Please Enter Valid E-mail Contains @ and .com : ").lower()
    return email
def validate_password():
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
    password = input(" NOTE--> Password should contain\n -lowercase, uppercase, number,special-char and should be at least 8 char \n Please Enter Your Password :  ").strip()
    while True:
        if(re.fullmatch(regex, password)):
            pass_confirm = input(" Please Enter password again : ")
            if password != pass_confirm:
                print("Please confirm your password to be the same")
            else:
                break
        else:
            print("Invalid password")
            password = input(" Please Enter valid Password :  \n Password should contain\n -lowercase, uppercase, number,special-char and should be at least 8 digits ").lower()
    return password
def validate_phone():
    phone = input("Note --> Enter 11 Digits Starts [validated against Egyptian phone numbers] \n Please enter your number : ").lower()
    while True:
        if len(phone) == 11 and phone.isnumeric():
            break
        else:
            print("Please Enter a Valid Egyptian Number")
            phone = input("Enter 11 Digits Starts [validated against Egyptian phone numbers] \n Please enter your number :  ").lower()
    return phone
