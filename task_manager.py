import os
import datetime
import time


# Function created to count the number of users.
def count_users():
    # Initialize for loop to 0 to count users.
    user_count = 0
    with open('user.txt', 'r') as f:
        # For Loop to initialize, and increment count.
        for _ in f:
            user_count += 1
    return user_count


# Function to count the number of tasks.
def count_tasks():
    # Initialize for loop to 0 to count tasks.
    task_count = 0
    with open('task.txt', 'r') as f:
        # For Loop condition & increment count.
        for _ in f:
            task_count += 1
    return task_count


# Existing usernames & passwords from file.
existing_usernames = []
    with open("user.txt", 'r', encoding='utf-8') as f:
        for line in f:
            temp = line.strip().split(',')
            existing_usernames.append(temp[0])
        existing_passwords.append(temp[1])


# User login section, using infinte loop.
while True:
    username = input('Enter username: ').lower()
    password = input('Enter password: ')

    if username in existing_usernames:
        if password == existing_passwords[existing_usernames.index(username)]:
            print('Login successful!')
            break
        else:
            print('Invalid password!!!')
            print('Please try again.')
    else:
        print('Invalid username!!!')
        print('Please try again.')


# Main menu loop.
while True:
    # Present Menu, Request User to input choice.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        # If statement to exclusively allow 'admin' to register users
        if input('Administrative username: ') == 'admin' and input("Administrative password: ") == 'admin':
            print('Admin access accepted:')
            print("To register a new user, please provide the following details:")
            username = input('Enter username: ').lower()

            if username in existing_usernames:
                print('Username already exists.')
            else:
                password = input('Enter password: ')
                
                # Open file to add registred username & password
                with open('user.txt', 'a') as f:
                    f.write(f'{username},{password}\n')
                print(f'{username} registered successfully!')
        else:
            print("Only 'admin' can register users.")

    # Elif user inputs 'a' request user iputs for all info for task.
    elif menu == 'a':
        
        title = input('Title of task: ')

        task_user = input('Username of task assignee: ').lower()

        description = input('Description: ')

        due_date = input('Due date (DD-MM-YYYY): ')

        current_date = datetime.date.today()

        # Include all data to task.txt file.
        with open('task.txt', 'a') as f:
            f.write(f'{task_user},{title},{description},{due_date},n\n')

        print("Task added successfully!!! at", current_date)
        print()

    # Elif user input va show all tasks using for loop.
    elif menu == 'va':
        # Read 'task.txt' file.
        with open('task.txt', 'r') as f:
            # For loop for task format.
            for line in f:
                # Split line for readability.
                title, username, description, due_date, status = line.strip().split(',')

                # Print task format.
                print(f'Username: {username}')
                print(f'Title: {title}')
                print(f'Description: {description}')
                print(f'Due date: {due_date}')
                print(f'Status: {status}')
                print()

    # Elif user inputs 'vm' show personal task of user.
    elif menu == 'vm':
        # Read 'task.txt' file and display tasks for the specific user.
        print(f"Tasks assigned to {username}:")
        with open('task.txt', 'r') as f:
            for line in f:
                # Split line for readability.
                task_user, title, description, due_date, status = line.strip().split(',')

                # Confirm if Username matches file.
                if task_user == username:
                    # Print task format.
                    print(f'Title: {title}')
                    print(f'Description: {description}')
                    print(f'Due date: {due_date}')
                    print(f'Status: {status}')
                    print()
    elif menu == 'e':
        print('Goodbye!!!')
        break
    else:
        print('Invalid option. Please try again.')

    input("Press Enter to continue...")

    # Timer to clear console and reset.
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')