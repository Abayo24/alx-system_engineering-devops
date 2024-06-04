#!/usr/bin/python3

"""
Python script that, using this REST API, exports data in the CSV format
"""


import csv
import requests
import sys


def export_to_csv(employee_id):
    """Fetch employee data and export to CSV"""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            )

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    employee_name = user_response.get('name')
    user_id = user_response.get('id')

    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_response:
            writer.writerow([
                user_id,
                employee_name,
                todo.get('completed'),
                todo.get('title')
                ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CVS.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    export_to_csv(employee_id)
