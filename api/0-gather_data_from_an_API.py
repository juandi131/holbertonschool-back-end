#!/usr/bin/python3
""" gather data from an API """


import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    tasks = requests.get(f"https://jsonplaceholder.typicode\
.com/users/{argv[1]}/todos")
    for user in users.json():
        if user['id'] == int(argv[1]):
            us = user
            break
        else:
            us = None
    doneTasks = []
    for task in tasks.json():
        for key, value in task.items():
            if key == 'completed':
                if value is True:
                    doneTasks.append(task)
    if us is not None:
        print(f"Employee {us['name']} is done \
with tasks({len(doneTasks)}/{len(tasks.json())}):")
        for title in doneTasks:
            for key, value in title.items():
                if key == 'title':
                    print(f"\t {value}")
