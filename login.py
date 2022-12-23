from Projects import projects
import os
def login():
    if os.path.getsize("users.txt") == 0:
        print("There is no users yet, Please sign up first \n")
    else:
        login_email = input("Please Enter Your E-mail : ").lower()
        try:
            with open("users.txt", 'r') as user:
                data = user.read()
                data = data.split(":")
        except:
            print("Something went Wrong ")
        else:
            while True:
                if login_email in data:
                    passuser = input("Please Enter Your Password : ")
                    if data[data.index(login_email)+1] == passuser:
                        print(f"\n Welcome {data[data.index(login_email)-2]} {data[data.index(login_email)-1]}\n")
                        try:
                            projects(data[0])
                        except:
                            print("Something went wrong")
                        break
                    else:
                        print("Please Enter valid Password , try again")
                else:
                    print("Please Enter valid E-mail , try again")
                    login_email = input("Please Enter Your E-mail : ").lower()