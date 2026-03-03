#!/usr/bin/python3
"""
Gather data from API and display employee information.
"""
import requests
import sys


if __name__ == "__main__":
    """ main section """
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/').json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        BASE_URL + f'/users/{sys.argv[1]}/todos').json()
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_LEN = len([k for k, v in serialized_todos.items() if v is True])
    TOTAL_TASKS = len(serialized_todos)

    print("Employee Name: {}".format(EMPLOYEE_NAME))
    print("To Do Count: {}".format(TOTAL_TASKS))
