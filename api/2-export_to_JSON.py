#!/usr/bin/python3
""" gather data from an API """


import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get(f"https://jsonplaceholder.typicode.com/users\
/{argv[1]}")
    tasks = requests.get(f"https://jsonplaceholder.typicode\
.com/users/{argv[1]}/todos")
    Save = []
    for task in tasks.json():
        newTask = {'task': f'{task.get("title")}',
                   'completed': task.get('completed'),
                   'username': f'{users.json().get("username")}'}
        Save.append(newTask)
    dictt = {f"{argv[1]}": Save}
    with open(f"{argv[1]}.json", 'w') as file:
        json.dump(dictt, file)
