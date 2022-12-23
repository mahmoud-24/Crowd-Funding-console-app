import datetime

def validate_name():
    project_name = input(" Please Enter your Project Name : ").strip().lower()
    while True:
        if project_name.isalpha():
            break
        else:
            print("Project name cannot Contain spaces ")
            project_name = input(" Please Enter your project name : ").strip().lower()
    return project_name

def validate_details():
    project_details = input(" Please Enter  project details : ").strip().lower()
    while True:
        if project_details.isalpha():
            break
        elif project_details == " ":
            print(" Project details cannot be Empty ")
            project_details = input(
                "Please Enter  project details : ").strip().lower()
        else:
            print("Project details cannot contain Digits , just use ',' ")
            project_details = input(
                "Please Enter  project details : ").strip().lower()
    return project_details

def validate_total_target():
    while True:
        total_target = int(input(" Please Enter your Total Target : "))
        if total_target >= 2000:
            break
        else:
            print(" Please enter target number above 2000")
            total_target  = input(" Please Enter your Total Target : ")
    return total_target 
#Set start/end time for the campaign (validate the date formula) 
#validate date function
def validate_date():
    while True:
        try:
            project_start_Date = input(
                " Please Enter project start date in 'dd-mm-yy' format : ").split('-')
            project_end_Date = input(
                " Please Enter project end date in 'dd-mm-yy' format : ").split('-')
            project_start_Date = datetime(int(project_start_Date[2]), int(
                project_start_Date[1]), int(project_start_Date[0]))
            try:
                project_end_Date = datetime(int(project_end_Date[2]), int(
                    project_end_Date[1]), int(project_end_Date[0]))
            except:
                print("Input date is not valid")
                break
        except:
            print("Input date is not valid")
            break
        else:
            if project_start_Date < project_end_Date:
                return [project_start_Date, project_end_Date]
            else:
                print("Input date is not valid")
                break
    return [project_start_Date, project_end_Date]

def validate_fields(id, line):
    edited_line = []
    fields = ["name", "details","target", "startdate", "enddate"]
    edited_field = input("Enter the field name to be edited from [ 'name', 'details','target', 'startdate', 'enddate'] :").strip().lower()
    if edited_field in fields:
        if edited_field == "name":
            projectname = validate_name()
            line[1] = projectname
            edited_line.append(line)
            return edited_line[0]
        elif edited_field == "details":

            project_details = validate_details()
            line[2] = project_details
            edited_line.append(line)
            return edited_line[0]
        elif edited_field == "target":

            target = str(validate_total_target())
            line[3] = target
            edited_line.append(line)
            return edited_line[0]
        elif edited_field == "startdate" or edited_field == "enddate":
            
            project_start_Date = str(validate_date()[0])
            project_end_Date = str(validate_date()[1])
            line[4] = project_start_Date
            line[7] = project_end_Date
            edited_line.append(line)
            return edited_line[0]
    else:
        print(" ERROR ")