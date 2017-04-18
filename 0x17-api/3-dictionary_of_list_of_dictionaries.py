#!/usr/bin/python3
"""
This modules creates a .json of employee data based on id
"""
import json
import requests
import sys


def get_user_info_json(user_id):
    """
    gets the users info and saves to .json
    """
    url_root = "https://jsonplaceholder.typicode.com"
    url_users = url_root + "/users"
    url_todos = url_root + "/todos"
    name = requests.get("{}/{}".
                        format(url_users, user_id)).json().get("username")
    r = requests.get("{}/?userId={}".format(url_todos, user_id)).json()
    with open("todo_all_employees.json".format(user_id), "a", newline="") as f:
        json.dump({user_id: [
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": name}
            for task in r]}, f)

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for user in users:
        get_user_info_json(user.get("id"))
