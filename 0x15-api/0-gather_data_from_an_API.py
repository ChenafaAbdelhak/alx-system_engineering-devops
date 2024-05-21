#!/usr/bin/python3
import requests
import sys

"""
Script to fetch and display the progress of a specific employee's tasks
from a JSONPlaceholder API.
"""

url = "https://jsonplaceholder.typicode.com"


def fetch_data_API(emp_id):
    """fetch data from an API"""
    user_url = "{}/users/{}".format(url, emp_id)
    todos_url = "{}/todos?userId={}".format(url, emp_id)

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user info for EMPLOYEE_ID:{employee_id}")
        return

    EMP_NAME = user_response.json().get("name")

    ALL_TASKS_NUMBER = 0
    DONE_TASKS_NUMBER = 0
    TASK_TITLE = []

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch todos for <EMPLOYEE_ID>: {employee_id}")
        return

    for task in todos_response.json():
        ALL_TASKS_NUMBER += 1
        if task.get("completed"):
            DONE_TASKS_NUMBER += 1
            TASK_TITLE.append(task.get("title"))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            EMP_NAME, DONE_TASKS_NUMBER, ALL_TASKS_NUMBER
        )
    )
    for task in TASK_TITLE:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <EMPLOYEE_ID>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("<EMPLOYEE_ID> must be an integer.")
        sys.exit(1)

    fetch_data_API(employee_id)
