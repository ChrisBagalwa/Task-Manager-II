# This program helps a small business to manage tasks assigned to each member of the team.
# Author: Chris Bagalwa
# 30/05/2022

# Importing datetime librarie
from datetime import datetime
# Define reg_user function
# Check if the user is admin
# If Yes, allow the user to add a new users's login details
def reg_user():
    # Check user, if username is "admin" then the if block execute otherwise the else block execute
    if username == "admin":
        new_user = False
        users_name = input("Please enter new user's username: ")
        register = open("user.txt", "r+")
        lines = register.readline()
        # Loop through the lines until end of file
        # If a user tries to add a username that already exists in user.txt, 
        # Provide a relevant error message and allow them to try with a different username.
        while lines:
            ext_user,ext_password = lines.split(", ")
            lines = register.readline()
            if ext_user == users_name:
                print("The entered user name already exists. Please pick a different name")
                new_user = True
                reg_user()
        register.close()
        # Loop through until new_userLogin get true
        while new_user == False:
            users_password = input("Please enter new user's password: ")
            confirm_password = input("Please confirm new user's password: ")
            if users_password == confirm_password:
                new_user = True
            if users_password != confirm_password:
                print("Password do not match. Enter again")
            if users_password == confirm_password:
                print("Password matches. New user has been created")
                append_me = open("user.txt", "a")
                append_me.write("\n" + str(users_name) + ", " + str(confirm_password))
                append_me.close()
    if username != "admin":
        print("Sorry, only admin user can add a new user.")
# Define add_task function
# Allow the user to add a new task to task.txt file
# Open tasks.txt file and prompt the user to enter the following:
# task_assignee, task_title, task_description, due_date, date_assigned, task_completed
# Then write data to the tasks.txt file
def add_task():
    tasks = open("tasks.txt","a")
    task_assignee = input("Enter the usersname of assignee: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter task description: ")
    due_date = input("Enter task due date in this format dd-MonthName-yyyy: ")
    date_assigned = datetime.now()
    task_completed = "No"
    tasks.write("\n" + str(task_assignee) + ", " + str(task_title) + ", " 
    + str(task_description) + ", " + str(date_assigned.strftime("%d %b %Y")) + ", " 
    + str(due_date) + ", " + str(task_completed))
    tasks.close()
# Define view_all function
# Read a line from the task.txt file, split that line where there is comma and space
# Then print as per the specified format
def view_all():
    view_tasks = open("tasks.txt","r+")
    for line in view_tasks:
        task_assignee, task_title, task_description, date_assigned, due_date, task_completed = line.split(", ")
        print(f'''
Assigned to:        {task_assignee}
Task:               {task_title}
Task description:   {task_description}
Date assigned:      {date_assigned}
Due date:           {due_date}
Task complete?:     {task_completed}''')
    view_tasks.close()
# Define view_mine function
# Read a line from the task.txt file, split that line where there is comma and space
# Check if the username of the person logged in is the same as the username you have read from the file
# If Yes, print the task as per the specified format
def view_mine():
    print(f"These are all the current tasks for {username}\n")
    num_task = 0
    view_mytasks = open("tasks.txt","r+")
    for line in view_mytasks:
        task_assignee, task_title, task_description, date_assigned, due_date, task_completed = line.split(", ")
        num_task += 1
        if username == task_assignee:
            print(f'''
Task number:        {str(num_task)}
Assigned to:        {task_assignee}
Task:               {task_title}
Task description:   {task_description}
Date assigned:      {date_assigned}
Due date:           {due_date}
Task complete?:     {task_completed}''')
    user_choice = int(input(f'''\nEnter one of the following:
To return to main menu: -1
To edit a task: Specify the task number
Choice: '''))
    if user_choice == -1:
        login = False
    # Iterate through the tasks.txt file and breaks at the task where the user selected
    else:
        count = 1
        txt_file = open("tasks.txt","r+")
        for line in txt_file:
            if count < user_choice:
                count += 1
            else:
                break
        edit_assignee, edit_title, edit_description, edit_date_assigned, edit_due_date, edit_task_completed = line.split(", ",6)
        edit_task_completed = edit_task_completed.replace("\n"," ")
        print(f'''
Assigned to:        {edit_assignee}
Task:               {edit_title}
Task description:   {edit_description}
Date assigned:      {edit_date_assigned}
Due date:           {edit_due_date}
Task complete?:     {edit_task_completed}''')
        # Prompt the user to enter if they want to edit a task or mark it as complete
        edit_mark = input('''\nDo you want to edit a task or mark it as complete? 
To edit a task assignee or due date: edit
To mark as completed: mark 
Choice: ''').lower()
        edit_task_completed = task_completed.lower()
        # If the user selects edit and the task has not being completed, 
        # the user gets asked what he wants to edit
        # The task then gets changed in the file, by locating its position and swapping the value
        if edit_mark == 'edit':
            choose_edit = input('''\nDo you want to edit the task assignee or the due date?
To edit task assignee: user
To edit due date: date
Choice: ''').lower()
            if choose_edit == 'user' and edit_task_completed == 'no':
                change_user = input('\nWho do you want to assign the task to?: ').lower()
                edit_assignee = change_user
                to_write = (edit_assignee + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned 
                + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
                write_task = open('tasks.txt', 'r+')
                write_file = write_task.readlines()
                write_file[count - 1] = to_write
                write_task = open('tasks.txt', 'w')
                write_task.writelines(write_file)
                write_task.close()
                print(f'The user has being changed to {edit_assignee}')
            elif choose_edit == 'date':
                change_date = input('\nWhat would you like to make the new due date? ').lower()
                edit_due_date = change_date
                to_write = (edit_assignee + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned 
                + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
                write_task = open('tasks.txt', 'r+')
                write_file = write_task.readlines()
                write_file[count - 1] = to_write
                write_task = open('tasks.txt', 'w')
                write_task.writelines(write_file)
                write_task.close()
                print(f'The due date has being changed to {edit_due_date} ')
        # If the user selected to mark the task as complete, the 'no' value will be changed to 'yes'
        # then it writes back into the file by locating its position
        elif edit_mark == 'mark':
            edit_task_completed = 'yes'
            to_write = (edit_assignee + ', ' + edit_title + ', ' + edit_description + ', ' + edit_date_assigned
            + ', ' + edit_due_date + ', ' + edit_task_completed + '\n')
            write_task = open('tasks.txt', 'r+')
            write_file = write_task.readlines()
            write_file[count - 1] = to_write
            write_task = open('tasks.txt', 'w')
            write_task.writelines(write_file)
            write_task.close()
            print('Task marked complete')
    view_mytasks.close()
# Define the generate report function and 
# Generate the task_overview text and user_overview file 
def generate_report():
    # Generate the task_overview.txt report
    with open("tasks.txt","r") as tasks:
        num_tasks = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0
        overdue_uncompleted = 0
        # Loop through tasks_line in tasks and increment the number of tasks
        for tasks_line in tasks:
            num_tasks += 1
            tasks_line = tasks_line.rstrip()
            tasks_line = tasks_line.split(", ")
            datetime_object = datetime.strptime(tasks_line[4],'%d %b %Y')
            # Use the if staement to check if the task is completed or not
            if tasks_line[5] == 'Yes':
                completed_tasks += 1
            if tasks_line[5] == 'No':
                uncompleted_tasks += 1
            # Compare the dates to check if the task is overdue.
            if datetime_object < datetime.today(): 
                overdue_tasks += 1
            if datetime_object < datetime.today() and tasks_line[5] == 'No':
                overdue_uncompleted += 1
        # Compute percentages for incomplete and overdue tasks
        pct_incomplete = round((uncompleted_tasks / num_tasks) * 100)
        pct_overdue = round((overdue_tasks / num_tasks) * 100)
        # Open the file, or creates it if it doesn't exist.
        # Generate the task_overview.txt file.
        with open('task_overview.txt', 'w+', encoding='utf-8') as task_overview:
            # Write everything to the file.
            task_overview.write(f"The total number of tasks: {num_tasks}\n")
            task_overview.write(f"The total number of completed tasks: {completed_tasks}\n")
            task_overview.write(f"The total number of uncompleted tasks: {uncompleted_tasks}\n")
            task_overview.write(f"The total number of uncompleted tasks that are overdue: {overdue_uncompleted}\n")
            task_overview.write(f"The percentage of tasks that are incomplete: {pct_incomplete:.0f}%\n")
            task_overview.write(f"The percentage of tasks that are overdue: {pct_overdue:.0f}%\n")
            print("Task_overview.txt written.")
    # Generate the user_overview.txt report
    with open("user.txt","r+") as users:
        num_users = 0
        # Loop through the users_line in users and increment the number of users
        for users_line in users:
            num_users += 1
            users_line = users_line.rstrip()
            users_line = users_line.split(", ")
            # Read the task.txt file
            with open("tasks.txt","r") as tasks:
                user_tasks = 0
                user_completed = 0
                user_incompleted = 0
                user_overdue_uncompleted = 0
                # Loop through the tasks_line in tasks and assignee tasks per user
                for tasks_line in tasks:
                    tasks_line = tasks_line.rstrip()
                    tasks_line = tasks_line.split(", ")
                    datetime_object = datetime.strptime(tasks_line[4], '%d %b %Y')
                    # Use the if staement to check if meets condition and if yes, increment by one
                    if users_line[0] == tasks_line[0]:
                        user_tasks += 1
                    if users_line[0] == tasks_line[0] and tasks_line[5] == 'Yes':
                        user_completed += 1
                    if users_line[0] == tasks_line[0] and tasks_line[5] == 'No':
                        user_incompleted += 1
                    if datetime_object < datetime.today(): 
                        overdue_tasks += 1
                    if users_line[0] == tasks_line[0] and datetime_object < datetime.today() and tasks_line[5] == 'No':
                        user_overdue_uncompleted += 1
                    else:
                        continue
            # If user has no task assigned to, skip to else statemen
            if user_tasks == 0:
                continue
            # Compute percentages for complete, incomplete, user and overdue tasks
            else:
                pct_user_completed = round((user_completed / user_tasks) * 100)
                pct_user_incomplete = round((user_incompleted / user_tasks) * 100)
                pct_user_tasks = round((user_tasks / num_tasks) * 100)
                pct_overdue_uncompleted = round((user_overdue_uncompleted / user_tasks) * 100)
                with open('user_overview.txt', 'a', encoding='utf-8') as user_overview:
                    # write everything to the user_overview file.
                    user_overview.write(f"Username: {users_line[0]}\n")
                    user_overview.write(f'The total number of tasks that have been generated: {num_tasks}\n')
                    user_overview.write(
                        f"The total number of tasks assigned to that user: {user_tasks}\n")
                    user_overview.write(
                        f"Percentage of the number of tasks assigned to the user: {pct_user_tasks:.0f}%\n")
                    user_overview.write(
                        f"Percentage of completed tasks assigned to user: {pct_user_completed:.0f}%\n")
                    user_overview.write(
                        f"Percentage of imcompleted tasks assigned to user: {pct_user_incomplete:.0f}%\n")
                    user_overview.write(
                        f"Percentage of imcompleted and overdue tasks assigned the user: {pct_overdue_uncompleted:.0f}%\n"
                        )
                    user_overview.write("\n")
        print("User_overview.txt written.")
# Define the display_admin_stats function that generate reports, two text files, 
# called task_overview.txt and user_overview.txt
# First call generate_report() function
def display_admin_stats():
    generate_report()
    task_stats = ""
    user_stats = ""
    # Display Task overview
    with open('task_overview.txt', 'r', encoding='utf-8') as task_overview:
        task_stats += task_overview.read()
        print(f'Task overview stats:\n{task_stats}\n')
    # Display Users overview per user
    with open('user_overview.txt', 'r', encoding='utf-8') as user_overview:
        user_stats += user_overview.read()
        print(f'Users overview stats:\n{user_stats}\n')
# Open user.txt file to allow login
# Provide the user with a menu option and convert to lower case
# If username is "admin" the menu should include the r,a,va,vm,gr,ds and e options
# Else the menu should only include the the a,va,vm, and e options
def login_menu(username):
        if username == "admin":
            print('''\nSelect one of the following Options below:
r - register user
a - add a task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit''')
        else:
            print('''\nSelect one of the following Options below:
a - add a task
va - view all tasks
vm - view my task
e - exit''')

login = False
# Use the while loop to validate the username and password
while login == False:
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    user_file = open("user.txt","r")
    text = user_file.readlines()
    for line in text:
        correct_user, correct_password = map(str.strip,line.split(","))
        if correct_user == username and correct_password == password:
            login = True
            print("Your login details are correct.")
            break
    else:
        print("Your login details are incorrect.\n")
user_file.seek(0)

login = True
while login:
    login_menu(username)
    menu = str(input("Please enter letter: ")).lower()
    if menu == 'r':
        reg_user()
    # Else if the user enters 'a', do the following:
    # Call add_task function
    elif menu == 'a':
        add_task()
    # Else if the user enters 'va', do the following:
    # Call view_all function
    elif menu == 'va':
        view_all()
    # Else if the user enters 'vm', do the following:
    # Call view_mine function
    elif menu == 'vm':
        view_mine()
    # Else if the user enters 'gr', do the following:
    # Call display_admin_stats
    elif menu == 'gr':
        generate_report()
    # Else if the user enters 'ds', do the following:
    # Call display_admin_stats
    elif menu == "ds":
        display_admin_stats()
    # Else if the user enters 'e', do the following:
    # Print 'Goodbye!!!' and exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # Else if the user makes a wrong choice from the menu option
    # Print 'You have made a wrong choice, Please Try again'
    else:
        print("You have made a wrong choice, Please Try again")