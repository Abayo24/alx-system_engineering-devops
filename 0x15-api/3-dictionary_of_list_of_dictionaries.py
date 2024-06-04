#!/usr/bin/python3

"""
Python script to export data in the JSON format.
Records all tasks from all employees
"""

import json
import requests


def fetch_data():
    """Base URLs"""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def create_todo_dict(users, todos):
    """Create a dictionary to hold user tasks"""
    todo_dict = {}

    user_map = {user['id']: user['username'] for user in users}

    for todo in todos:
        user_id = todo['userId']
        if user_id not in todo_dict:
            todo_dict[user_id] = []
        todo_entry = {
            'username': user_map[user_id],
            'task': todo['title'],
            'completed': todo['completed']
        }
        todo_dict[user_id].append(todo_entry)

    return todo_dict


def save_to_json(data, filename='todo_all_employees.json'):
    """Save the data to a JSON file"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    users, todos = fetch_data()
    todo_dict = create_todo_dict(users, todos)
    save_to_json(todo_dict)
