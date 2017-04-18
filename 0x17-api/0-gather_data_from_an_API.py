#!/usr/bin/python3
"""
This modules returns the to do list of an employee based on id
"""
import requests
import sys


def get_user_info(user_id):
    url_root = "https://jsonplaceholder.typicode.com"
    url_users = url_root + "/users"
    url_todos = url_root + "/todos"
    name = requests.get("{}/{}".format(url_users, user_id)).json().get("name")
    r = requests.get("{}/?userId={}".format(url_todos, user_id)).json()
    task_done = [task for task in r if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(task_done), len(r)))
    for task in task_done:
        print("\t{}".format(task.get("title")))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_user_info(sys.argv[1])
