from project_validation_functions import*
from create_project import*
from edit_project import*
from delete_project import*
from view_project import*


def projects(id):
    print(" Please Select one of the following :- ")
    while True:
        choice = int(input("\t\t1) Please Enter 1 to Create Project\n\t\t2) Please Enter 2 to Edit Project\n\t\t3) Please Enter 3 to Delete Project\n\t\t4) Please Enter 4 to View Projects\n\t\t5) Please Enter 5 to exit \n\t\t"))
        try:
            choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 
        except:
            print("Please Select one of the above ")
        else:
            if choice == 1:
                try:
                    createproject(id)
                except:
                    print("Something went wrong")
            elif choice == 2:
                try:
                    edit = edit_project(id)
                except:
                    print("Something went wrong")
                else:
                    with open("projects.txt", 'w') as projects_file:
                        projects_file.writelines(edit)
            elif choice == 3:
                try:
                    delete = deleteproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(delete)
            elif choice == 4:
                print(" Viewing projects \n")
                try:
                    view_project()
                except:
                    print("something went wrong")        
            elif choice == 5:
                print("Exiting")
                break
            else:
                print("Invalid choice")
