#!/usr/bin/python3
"""
Export all employees' tasks to JSON with proper formatting.
"""
import json
import requests


def get_all_employee_tasks():
    """
    Fetches all employees and their tasks from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users = requests.get(f"{base_url}/users").json()

    all_tasks = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]

        # Get all tasks for this user
        todos = requests.get(f"{base_url}/users/{user_id}/todos").json()

        # Format tasks as list of dictionaries
        task_list = []
        for task in todos:
            task_list.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

        all_tasks[str(user_id)] = task_list

    return all_tasks


if __name__ == '__main__':
    all_tasks = get_all_employee_tasks()

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f, indent=4)
