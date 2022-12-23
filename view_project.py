def view_project():
    projects_file = open("projects.txt", 'r')
    for line in projects_file:
        print(line)
