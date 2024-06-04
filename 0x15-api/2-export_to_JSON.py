#!/usr/bin/python3

"""
Python script that, using this REST API, exports data in the JSON format
"""


import json
import requests
import sys


def export_to_json(employee_id):
    """Fetch employee data and export to JSON"""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            )

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    username = user_response.get('username')
    user_id = user_response.get('id')

    tasks = [{
        "task": todo.get('title'),
        "completed": todo.get('completed'),
        "username": username
        } for todo in todos_response]

    data = {str(user_id): tasks}

    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    export_to_json(employee_id)
