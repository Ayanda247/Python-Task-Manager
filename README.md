# Task Manager

This is a simple task manager application written in Python that allows users to manage tasks and generate reports. The application supports functionalities such as registering users, adding tasks, viewing tasks, and generating reports. Only the admin user has the permission to register new users and view statistics.

## Features

- **Register User**: Only the admin user can register new users.
- **Add Task**: Users can add tasks with details such as title, description, assigned date, and due date.
- **View All Tasks**: View all tasks in the system.
- **View My Tasks**: View tasks assigned to the logged-in user.
- **View Statistics**: Only the admin user can view statistics about the number of users and tasks.
- **Generate Reports**: Only the admin user can generate reports about tasks and users.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your machine.

### Usage

1. Run the `task_manager.py` script.
2. Log in with a username and password. If you are the admin, use the username `admin`.

### Files

- `user.txt`: Stores the usernames and passwords of registered users.
- `tasks.txt`: Stores the details of tasks.
- `task_overview.txt`: Contains the report about tasks.
- `user_overview.txt`: Contains the report about users.

## Functions

### count_users
Reads from `user.txt` and counts the number of users.
```python
def count_users():
    # Returns the number of users in 'user.txt'
