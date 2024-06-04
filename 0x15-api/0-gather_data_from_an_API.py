#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    """gets emplyee data"""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            )

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    employee_name = user_response.get('name')
    total_tasks = len(todos_response)
    done_tasks = [todo for todo in todos_response if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with"
          f" tasks({number_of_done_tasks}/{total_tasks}): ")

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
