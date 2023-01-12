# Task-Manager-II
This program helps a small business to manage tasks assigned to each member of the team.
# Description
This program is a task management application that allows users to register, add tasks, view all tasks and view tasks assigned to them. The program also has an option for an admin user to generate reports and view statistics.

To get started, create a copy of the task_manager.py file and save it in a Dropbox folder. Also, copy and paste the user.txt and tasks.txt files that accompanied the previous Capstone project to the same Dropbox folder. Once all the files are in the correct location, run the task_manager.py file.

The program includes several functions to improve the modularity of the code. The reg_user() function is called when the user selects 'r' to register a user. This function checks if the input username already exists in the user.txt file. If it does, it provides an error message and prompts the user to try again with a different username. The add_task() function is called when a user selects 'a' to add a new task. The view_all() function is called when users type 'va' to view all the tasks listed in 'tasks.txt' and the view_mine() function is called when users type 'vm' to view all the tasks that have been assigned to them.

The view_mine() function allows the user to view all tasks assigned to them in a user-friendly manner, with each task displayed with a corresponding number for identification. The user can select a specific task by entering its number or input '-1' to return to the main menu. The user can also mark a task as complete or edit a task (username or due date) if it has not been completed yet.

The program also includes an option for an admin user to generate reports. When the user selects this option, the program generates the following text files in the same folder: task_overview.txt and user_overview.txt. The task_overview.txt file contains statistics on the total number of tasks and completed/uncompleted/overdue tasks. The user_overview.txt file contains statistics on the total number of users registered, tasks assigned to each user and their completion status.

The program also includes an option for the admin user to view statistics. If the task_overview.txt and user_overview.txt files do not exist, the program will first generate them before displaying the statistics on the screen in a user-friendly manner. It is important to note that the user.txt and tasks.txt files should be in the same folder as the task_manager.py file and should be readable by the program.
