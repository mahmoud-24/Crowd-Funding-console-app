def deleteproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        file = ""
        projectname = input("Please Enter your Project name to delete it : ").strip().lower()
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    print(" Project Deleted Successfully \n")
                else:
                    file += line    
            else:
                print("The Project Name you entered dosen't Exsist, Please Enter Valid Project Name ")
                file += line    
                break
        return file