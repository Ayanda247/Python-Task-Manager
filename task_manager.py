# Import Modules.
import os
import time
from datetime import datetime, date


# Function to count the number of users.
def count_users():
    """
    Reads from 'user.txt' and counts the number of users.

    Function description:
        Counts the number of users in the 'user.txt' file with loop and
        returns the count.


    Returns:
        Number of users in the 'user.txt' file.
    """

    # Generate user count from 'user.txt' with a with statement.
    user_count = 0
    with open("user.txt", "r", encoding="utf-8") as f:
        for _ in f:
            user_count += 1
    return user_count


# Function to count the number of tasks.
def count_tasks():
    """
    Counts the number of tasks in the 'tasks.txt' file.

    Function description:
        Counts the number of tasks in the 'tasks.txt' file and returns
        the count.

    Args:
        None

    Returns:
        Number of tasks in the 'tasks.txt' file.
    """

    # Generate task count from 'tasks.txt' with a with statement.
    task_count = 0
    with open("tasks.txt", "r", encoding="utf-8") as f:
        for _ in f:
            task_count += 1
    return task_count


# Function to clear the terminal screen.
def clear_screen():
    """
    Clears the terminal screen after 0.1 seconds.

    Function description:
        Clears the terminal screen using os.system() function.

    Args:
        None


    Returns:
        None
    """
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")


# Function to check if user exists.
def user_exists(username):
    """
    Checks if a user exists in the 'user.txt' file.

    Function Description:
        Checks if a user exists in the 'user.txt' file then uses with
        statement to check if user exists.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the user exists, False otherwise.
    """
    # Verifies if username exist in 'user.txt'  with a with statement.
    with open("user.txt", "r", encoding="utf-8") as f:
        for line in f:
            temp = line.strip().split(",")
            if temp[0] == username:
                return True
    return False


# Function to validate date format.
def validate_date(date_str):
    """
    Validates the date format.

    Function Description:
        Validates the date format using datetime.strptime() function.

    Args:
        date_str (str): The date string to validate.

    Returns:
        bool: True if the date format is valid, False otherwise.
    """

    now = date.today()

    # Validates format of date_str.
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        try:
            datetime.strptime(date_str, " %d %b %Y")
            return True
        except ValueError:
            return False


# Function to register a new user.
def reg_user():
    """
    Registers a new user by admin.

    Function description:
        Registers a new user by admin. Writes new_username in
        'user.txt' file to complete registration process.

    Args:
        None

    Returns:
        None
    """
    # If statment to check if user != 'admin.
    if username != "admin":
        print("Only 'admin' can register users.")
        return

    print("Admin access accepted:")
    new_username = input("Enter username: ").lower()

    if user_exists(new_username):
        print("Username already exists.")
        return

    new_password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    if new_password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    # Append new_username & new_password in 'user.txt' file (with statement).
    with open("user.txt", "a", encoding="utf-8") as f:
        f.write(f"{new_username},{new_password},\n")
    print(f"{new_username} registered successfully!")
    print("_" * 79)
    print()


# Function to add a task.
def add_task():
    """
    Adds a task to the tasks.txt file.

    Function description:
        Adds a task to the tasks.txt file. Requests user to input
        information for task. Then writes information to 'tasks.txt'
        file.

    Args:
        None

    Returns:
        None
    """

    # If statment to check if user != 'admin.
    if username == user_exists:
        print(f"{username}:" + "'s tasks:")

    title = input("Title of task: ")

    # If statment to check if title is empty.
    if title == "":
        print("Error: Title cannot be empty!")
        return

    task_user = input("Confirm Username of task assignee: ").lower()
    if not user_exists(task_user):
        print("Error: User does not exist!")
        return

    task_password = input("Confirm Password to Continue: ")
    if not password == task_password:
        print()
        return

    description = input("Description: ")

    if description == "":
        print("Error: Description cannot be empty!")
        return
    # Assigned_date_str variable stores assigned date of the task.
    assigned_date_str = input("Assigned date (DD-MM-YYYY): ")
    # Validate_date validates date format.
    if not validate_date(assigned_date_str):
        print("Invalid date format. Please use DD-MM-YYYY format.")
        return
    # Assigned_date variable stores assigned date of task as date object.
    assigned_date = datetime.strptime(assigned_date_str, "%d-%m-%Y").date()
    # Using date.today() directly.
    current_date = date.today()
    if assigned_date > current_date:
        print("Error: Assigned date cannot be in the future!")
        return

    due_date_str = input("Due date (DD-MM-YYYY): ")
    if not validate_date(due_date_str):
        print("Invalid date format. Please use DD-MM-YYYY format.")
        return

    # Stores due_date as date object.
    due_date = datetime.strptime(due_date_str, "%d-%m-%Y").date()
    if due_date < current_date:
        print("Error: Due date cannot be in the past!")
        return

    # Appends user inputs in 'tasks.txt' with a with statement.
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(
            f"{task_user},{title},{description},{due_date_str},{assigned_date_str},No\n"
        )

    print("Task added successfully!!! at", current_date)
    print("_" * 79)
    print()


# Function to view all tasks.
def view_all():
    """
    Views all tasks from the tasks.txt file.

    Function description:
        Views all tasks from the tasks.txt file. Iterates over each line in
        tasks.txt' file and print task information.

    Args:
        None

    Returns:
        None
    """
    print("All tasks:")
    # With statment reads 'tasks.txt' and extracts all tasks.
    with open("tasks.txt", "r") as f:
        for line in f:
            title, username, description, due_date_str, assigned_date_str, status = (
                line.strip().split(",")
            )
            print(f"Username: {username}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Due date: {due_date_str}")
            print(f"Assigned date: {assigned_date_str}")
            print(f"Status: {status}\n")

    print("_" * 79)
    print()

    """
    Updates task in 'tasks.txt' file.

        Function Description:
            Updates task in 'tasks.txt' file.
            
        Args:
            tasks (list): List of tasks to update.

        Returns:
            None
    """


# Function to update files within the task.
def update_task_in_file(tasks):
    # With statement opens 'tasks.txt' and writes data.
    with open("tasks.txt", "w", encoding="utf-8") as f:
        # Loop iterates over each task in 'tasks.txt' file.
        for task in tasks:
            f.write(
                f'{task["task_user"]},{task["title"]},{task["description"]},{task["due_date"]},{task["assigned_date"]},{task["status"]}\n'
            )


# Function to view user's task.
def view_mine():
    """
    Views tasks assigned to the current user.

    Function description:
        Views tasks assigned to the current user. Iterates over each
        line in 'tasks.txt' file and prints task information. Also keeps
        track of the number of tasks assigned to the current user throu-
        gh a for loop. Programs allows user to edit, mark as complete,
        and delete tasks assigned to them. Achieved through infinite
        loop and if statements that write to 'tasks.txt' file based on
        user inputs and returns to main menu.

    Args:
        None

    Returns:
        None
    """

    # If statment to check if user != 'admin.
    if username == user_exists:
        print(f"{username}" + "'s tasks:")

    task_user = input("Confirm Username of task assignee: ").lower()
    if not user_exists(task_user):
        print("Error: User does not exist!")
        return

    task_password = input("Confirm Password to Continue: ")
    if not password == task_password:
        print()
        return

    # Store 'tasks'.
    tasks = []
    user_task_count = 0
    # Reads 'tasks.txt' file.
    with open("tasks.txt", "r", encoding="utf-8") as f:
        # Iterate over each line to seperate pieces of data.
        for line in f:
            task_user, title, description, due_date_str, assigned_date_str, status = (
                line.strip().split(",")
            )
            if task_user == username:
                user_task_count += 1
                # Creates dictionary abd appended to tasks list.
                # Key value pairs of user inputs.
                tasks.append(
                    {
                        "task_user": task_user,
                        "title": title,
                        "description": description,
                        "due_date": due_date_str,
                        "assigned_date": assigned_date_str,
                        "status": status,
                        "index": user_task_count,
                    }
                )

    print("My tasks:")
    # Loop iterates over each task in 'task.txt' file.
    for task in tasks:
        print(f'{task["index"]}. {task["title"]}')
        print(f'Description: {task["description"]}')
        print(f'Due date: {task["due_date"]}')
        print(f'Assigned date: {task["assigned_date"]}')
        print(f'Status: {task["status"]}\n')

    print("_" * 79)
    print()
    # While true loop runs til user enters '-1'.
    while True:
        choice = input(
            "Select a task (enter its number) or -1 to return to the main menu: "
        )
        if choice == "-1":
            break
        # Checks if choice is a digit.
        elif choice.isdigit():
            choice = int(choice)
            # Checks if choice is within the range of tasks.
            if choice > 0 and choice <= len(tasks):
                task = tasks[choice - 1]
                # While loop performs m - Mark the task as completes.
                # While loop performs e - Edit the task.
                # While loop runs until -1 - Return to the main menu.
                while True:
                    action = input(
                        "Choose an action (m - mark as complete, e - edit, -1 to return): "
                    )
                    if action == "-1":
                        break
                    elif action == "m":
                        if task["status"] == "No":
                            task["status"] = "Yes"
                            # Function to update update_task_in_file() in task 'tasks.txt' file.
                            update_task_in_file(tasks)
                            print("Task marked as complete.")
                        else:
                            print("Task is already complete.")
                    elif action == "e":
                        # If statement checks if the task is not yet complete therefore can-
                        # not be edited.
                        if task["status"] == "No":
                            new_username = input("Enter new username: ")
                            # Verifies with if statement if new username is valid.
                            if user_exists(new_username):
                                task["task_user"] = new_username
                                print("Username updated.")
                            else:
                                print("Invalid username.")
                            new_due_date = input("Enter new due date (DD-MM-YYYY): ")
                            # Verifies if new_due_date is valid.
                            if validate_date(new_due_date):
                                task["due_date"] = new_due_date
                                print("Due date updated.")
                            else:
                                print(
                                    "Invalid date format. Please use DD-MM-YYYY format."
                                )
                            update_task_in_file(tasks)
                        else:
                            print("Cannot edit a completed task.")
                    else:
                        print("Invalid action. Please try again.")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

    print("_" * 79)
    print()


view_mine()


# Function to view statistics.
def view_statistics():
    """
    Views statistics about the number of users and tasks.

    Function description:
        Views statistics about the number of users and tasks. Displays
        the number of users and tasks in the system. Ensures that only
        admin can access statistics with if statement.

    Args:
        None

    Returns:
        None
    """
    # Verfies if user is 'admin'.
    if username != "admin":
        print("Only 'admin' can view statistics.")
        return

    print("Statistics:")
    print(f"Number of users: {count_users()}")
    print(f"Number of tasks: {count_tasks()}")

    print("_" * 79)
    print()


# Function to generate reports.
def generate_reports():
    """
    Generates text files containing reports about tasks and users.

    Function description:
        Generates text files containing reports about tasks and users.
        The task_overview.txt file includes information about the total
        number of tasks, the number of completed tasks, the number of
        uncompleted tasks, the number of overdue tasks, the percentage
        of incomplete tasks, and the percentage of overdue tasks.
        The user_overview.txt file includes information about the total
        number of users, the total number of tasks assigned to each user,
        the percentage of tasks assigned to each user, the percentage of
        completed tasks assigned to each user, the percentage of uncompleted
        tasks assigned to each user, and the percentage of overdue tasks
        assigned to each user.

    Args:
        None

    Returns:
        None
    """
    # Verifies if user is 'admin'.
    if username != "admin":
        print("Only 'admin' can generate reports.")
        return

    # Generate task_overview.txt
    with open("task_overview.txt", "w", encoding="utf-8") as f:
        total_tasks = count_tasks()
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0
        # With sattement  line opens the tasks.txt file in read mode.
        with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
            # Iterates over each line in file.
            for line in tasks_file:
                task_user, _, _, due_date_str, _, status = line.strip().split(",")
                # Verifies if status of task is not 'yes' meaning task is completed.
                if status == "Yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1
            # Using datetime.strptime() to parse the due date string only once.
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y").date()
            # Using date.today() directly.
            if due_date < date.today():
                overdue_tasks += 1
                print(
                    "Reports have been generated seek tasks_overview.txt and user_overview.txt for the full reports."
                )
                print()
        # Stores the percentage of incomplete tasks.
        # Performs formula (x/y) * 100 to get percentage(%).
        percent_incomplete_tasks = (uncompleted_tasks / total_tasks) * 100
        percent_overdue_tasks = (overdue_tasks / total_tasks) * 100

        # Writes task_overview.txt report.
        f.write(f"Total number of tasks: {total_tasks}\n")
        f.write(f"Number of completed tasks: {completed_tasks}\n")
        f.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Number of overdue tasks: {overdue_tasks}\n")
        f.write(f"Percentage of incomplete tasks: {percent_incomplete_tasks:.2f}%\n")
        f.write(f"Percentage of overdue tasks: {percent_overdue_tasks:.2f}%\n")

    print("_" * 79)
    print()

    # Generates user_overview.txt with a with statement.
    with open("user_overview.txt", "w", encoding="utf-8") as f:
        total_users = count_users()

        # Contains user input dictionary with keys that are the
        # Usernames of the users, and the values will be the number of
        # Tasks assigned to each user.

        user_tasks = {}
        with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
            for line in tasks_file:

                task_user, _, _, _, _, _ = line.strip().split(",")
                # Checks if task_user is already a key in user_tasks.
                if task_user not in user_tasks:
                    # CountS number of tasks assigned to each user.
                    user_tasks[task_user] = 0
                user_tasks[task_user] += 1

        f.write(f"Total number of users: {total_users}\n")
        # Iterates over user_tasks, key: user & value: user_tasks.
        for user in user_tasks:
            # Writes Username, total number of tasks and Percentage.
            f.write(f"Username: {user}\n")
            f.write(f"Total number of tasks assigned: {user_tasks[user]}\n")
            # Performs formula (x/y) * 100 to get percentage(%).
            f.write(
                f"Percentage of tasks assigned: {(user_tasks[user] / total_tasks) * 100:.2f}%\n"
            )
            completed_tasks = 0
            with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                for line in tasks_file:
                    task_user, _, _, _, _, status = line.strip().split(",")
                    # Verifies if status == 'yes'.
                    if task_user == user and status == "Yes":
                        # Increments the completed_tasks variable.
                        completed_tasks += 1
                        print(
                            "Reports have been generated seek tasks_overview.txt and user_overview.txt for the full reports."
                        )
                        # Calculates percentage of completed task.
                        # Formula (x/y) * 100 to get percentage(%).
            f.write(
                f"Percentage of completed tasks: {(completed_tasks / user_tasks[user]) * 100:.2f}%\n"
            )
            # Calculates percentage of uncompleted task.
            # Formula (x/y) * 100 to get percentage(%).
            f.write(
                f"Percentage of uncompleted tasks: {((user_tasks[user] - completed_tasks) / user_tasks[user]) * 100:.2f}%\n"
            )
            overdue_tasks = 0
            with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                for line in tasks_file:
                    # Verifies if task_user value is equal to user.
                    task_user, _, _, due_date, _, _ = line.strip().split(",")
                    # Using date.today() directly.
                    # Verifies if the due_date value is less than
                    # Current date.
                    if (
                        task_user == user
                        and datetime.strptime(due_date, "%d-%m-%Y").date()
                        < date.today()
                    ):
                        overdue_tasks += 1
            # Calculatespercentage of overdue_tasks dividing overdue_tasks by.
            # user_tasks[user].
            # Writes the percentage of overdue tasks to user_overview.txt.
            f.write(
                f"Percentage of overdue tasks: {(overdue_tasks / user_tasks[user]) * 100:.2f}%\n\n"
            )

    print("_" * 79)
    print()

    print()
    # Generate user_overview.txt with a with statement.
    with open("user_overview.txt", "w", encoding="utf-8") as f:
        total_users = count_users()

        user_tasks = {}
        with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
            for line in tasks_file:
                task_user, _, _, _, _, _ = line.strip().split(",")
                # Verifies if the task_user is already key in user_tasks.
                if task_user not in user_tasks:
                    user_tasks[task_user] = 0
                # Increments the value of the task_user key by 1.
                user_tasks[task_user] += 1

        f.write(f"Total number of users: {total_users}\n")
        for user in user_tasks:
            f.write(f"Username: {user}\n")
            # Writes & calculates total number of users,total number of tasks of
            # each user.
            f.write(f"Total number of tasks assigned: {user_tasks[user]}\n")
            # Writes & calculates percenatge of tasks formula (x/y) * 100.
            f.write(
                f"Percentage of tasks assigned: {(user_tasks[user] / total_tasks) * 100:.2f}%\n"
            )
            completed_tasks = 0
            with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                for line in tasks_file:
                    task_user, _, _, _, _, status = line.strip().split(",")
                    # If statement status == 'yes'
                    if task_user == user and status == "Yes":
                        # Increments completed tasks by 1.
                        completed_tasks += 1
                        print(
                            "Reports have been generated seek tasks_overview.txt and user_overview.txt for the full reports."
                        )
                        print()
                        # Writes & calculates percentage of completed
                        # task.Formula (x/y) * 100 to get percentage(%).
            f.write(
                f"Percentage of completed tasks: {(completed_tasks / user_tasks[user]) * 100:.2f}%\n"
            )
            #  Writes & calculates percentage of uncompleted
            # task.Formula (x/y) * 100 to get percentage(%).
            f.write(
                f"Percentage of uncompleted tasks: {((user_tasks[user] - completed_tasks) / user_tasks[user]) * 100:.2f}%\n"
            )
            overdue_tasks = 0
            with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                for line in tasks_file:
                    task_user, _, _, due_date, _, _ = line.strip().split(",")
                    if (
                        task_user == user
                        and datetime.strptime(due_date, "%d-%m-%Y").date()
                        < date.today()
                    ):

                        overdue_tasks += 1
            f.write(
                f"Percentage of overdue tasks: {(overdue_tasks / user_tasks[user]) * 100:.2f}%\n\n"
            )

    print("_" * 79)
    print()


# Main program loop
username = None
while True:
    # Request username
    if username is None:
        username = input("Enter username: ").lower()

    # Request password if username exist within 'user.txt'.
    if user_exists(username):
        password = input("Enter password: ")
        with open("user.txt", "r", encoding="utf-8") as f:
            for line in f:
                if username in line:
                    if password in line:
                        print("Login successful!")
                        break
                    else:
                        print("Invalid password!!!")
                        print("Please try again.")
        break
    else:
        print("Invalid username!!!")
        print("Please try again.")
        username = None

    print("_" * 79)
    print()

# Main menu loop
while True:
    # Display options for inputs.
    menu = input(
        """Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vs - view statistics
gr - generate reports
e - exit
: """
    ).lower()

    print("_" * 79)

    if menu == "r":
        reg_user()
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()
    elif menu == "vs":
        view_statistics()
    elif menu == "gr":
        generate_reports()
    elif menu == "e":
        print("Goodbye!!!")
        break
    else:
        print("Invalid option. Please try again.")

    print()
    print("_" * 79)

    input("Press Enter to continue")
    print("..................!!!LOADING!!!..................")

    clear_screen()
    print("_" * 79)
    print()
