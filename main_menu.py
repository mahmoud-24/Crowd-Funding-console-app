from user_validation_function import *
from login import *
from registration import*

def register():
    print("\t\t\tWelcome to Crowd Funding Console App")
    print(" Select one of the following options :- \n")
    choice = int(input("\t1) Please Enter 1 to login \n\t2) Please Enter 2 to Signup \n "))
    try:
        choice == 1 or choice == 2
    except:
        print("Please Enter 1 to login  or 2 to sign up ")
    else:
        if choice == 1:
            try:
                login()
            except:
                print("Something went wrong")
        elif choice == 2:
            try:
                registration()
            except:
                print("Something went wrong")
        else:
            print("Invalid Choice")

register()
