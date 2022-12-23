from project_validation_functions import*

def createproject(id):
    project_name = validate_name()
    project_details = validate_details()
    target = validate_total_target()
    project_start_Date = validate_date()[0]
    project_end_Date = validate_date()[1]
    print(" Project Successfully Created")
    print(f" Project Name : {project_name} \n Project Details : {project_details} \n Project Total_Target : {target} \n Project_Start_Date : {project_start_Date} \n Project_end_date : {project_end_Date} ")

    with open("projects.txt", 'a') as projects_file:
        projects_file.writelines(
            [f"{id}:{project_name}:{project_details}:{target}:{project_start_Date}:{project_end_Date} \n"]
        )