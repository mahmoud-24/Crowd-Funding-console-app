from project_validation_functions import *

def edit_project(id):
    while True:
        projects_file = open("projects.txt", 'r')
        file = ""
        project_name = input(
            "PLease Enter your project name to Edit : ").lower()
        for line in projects_file.readlines():
            if id in line:
                if line.split(":")[1] == project_name:
                    edited_line = validate_fields(id, line.split(":"))
                    edited_line = ":".join(edited_line)
                    file += edited_line
                    print("Project Edited Successfully \n")
                else:
                    file += line
            else:
                print("Please Enter exsist Project name ")
                file += line
        return file
