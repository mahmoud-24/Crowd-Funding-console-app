from user_validation_function import *
from login import *

def registration():
    fullname = validate_name()
    with open("users.txt", 'a') as user:
        user.writelines(
            [f"{id(fullname)}:{fullname[0]}:{fullname[1]}:"])

    email = validate_email()
    with open("users.txt", 'a') as user:
        user.write(f"{email}:")

    password = validate_password()
    with open("users.txt", 'a') as user:
        user.write(f"{password}:")

    phone = validate_phone()
    with open("users.txt", 'a') as user:
        user.write(f"{phone}\n")

    print(" Registration Successfully Done ")
    choiceforlogin = input("Do you want to Login Now?[y/n] ").strip().lower()
    try:
        choiceforlogin == "y" or choiceforlogin == "n"
    except:
        print(" Please Enter valid char (y) or (n)")
    else:
        if choiceforlogin == "y":
            login()
        elif choiceforlogin == "n":
            print(" Goodbye")
        else:
            print("Invalid input")