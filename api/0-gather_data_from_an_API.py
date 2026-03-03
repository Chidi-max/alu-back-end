#!/usr/bin/python3
"""
Gathers data from a REST API for a given employee ID
and displays their TODO list progress.
"""
import sys
import urllib.request
import json


def gather_data_from_an_API(employee_id):
    """
    Fetches employee information and their TODO list from the API.

    Args:
        employee_id: Integer ID of the employee
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee information
    employee_url = f"{base_url}/users/{employee_id}"
    with urllib.request.urlopen(employee_url) as response:
        employee_data = json.loads(response.read().decode())

    employee_name = employee_data['name']

    # Fetch TODO list for the employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = sum(1 for task in todos if task['completed'])

    # Display results in the required format
    print(
        f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in todos:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    # Check if employee ID is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    gather_data_from_an_API(employee_id)
