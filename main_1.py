#!/usr/bin/python3
"""
Export employee tasks to CSV file.
"""
import requests
import sys


if __name__ == "__main__":
    """ main section """
    EMP_ID = sys.argv[1]
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee = requests.get(
        BASE_URL + f'/users/{EMP_ID}/').json()
    EMPLOYEE_NAME = employee.get("username")
    employee_todos = requests.get(
        BASE_URL + f'/users/{EMP_ID}/todos').json()

    with open(str(EMP_ID) + '.csv', "w") as f:
        f.write("USER_ID,USER_NAME,TASK_COMPLETED,TASK_TITLE\n")
        for todo in employee_todos:
            f.write(
                '"' + str(EMP_ID) + '",' +
                '"' + EMPLOYEE_NAME + '",' +
                '"' + str(todo["completed"]) + '",' +
                '"' + todo["title"] + '",' + "\n"
            )
