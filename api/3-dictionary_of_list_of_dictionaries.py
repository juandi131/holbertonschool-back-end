#!/usr/bin/python3
""" gather data from an API """


import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get(f"https://jsonplaceholder.typicode.com/users")
    Save = {}
    for user in users.json():
        tasks = requests.get(f"https://jsonplaceholder.typicode\
.com/users/{user.get('id')}/todos")
        ta = []
        for task in tasks.json():
            newTask = {'username': f"{user.get('username')}",
                       'task': f"{task.get('title')}",
                       'completed': task.get('completed')}
            ta.append(newTask)
        Save[f"{user.get('id')}"] = ta

    with open("todo_all_employees.json", 'w') as file:
        json.dump(Save, file)
