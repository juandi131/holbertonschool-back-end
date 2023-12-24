#!/usr/bin/python3
""" gather data from an API """


import csv
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get(f"https://jsonplaceholder.typicode.com/users\
/{argv[1]}")
    tasks = requests.get(f"https://jsonplaceholder.typicode\
.com/users/{argv[1]}/todos")
    Save = []
    for task in tasks.json():
        newTask = [f'{users.json().get("id")}',
                   f'{users.json().get("username")}',
                   f'{task.get("completed")}',
                   f'{task.get("title")}']
        Save.append(newTask)
    with open(f"{argv[1]}.csv", 'w') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        write.writerows(Save)
