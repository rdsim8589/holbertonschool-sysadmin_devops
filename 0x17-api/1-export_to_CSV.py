#!/usr/bin/python3
"""
This module creates a .csv file of employee data based on id
"""
import csv
import requests
import sys


def get_user_info_csv(user_id):
    """
    Arguement: user_id

    output: csv file formatted as
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

    """
    url_root = "https://jsonplaceholder.typicode.com"
    url_users = url_root + "/users"
    url_todos = url_root + "/todos"
    name = requests.get("{}/{}".
                        format(url_users, user_id)).json().get("username")
    r = requests.get("{}/?userId={}".format(url_todos, user_id)).json()
    with open("{}.csv".format(user_id), "w", newline="") as f:
        csvwriter = csv.writer(f, delimiter=",", quotechar='"',
                               quoting=csv.QUOTE_ALL)
        csvwriter.writerows([user_id, name, task.get("completed"),
                            task.get("title")] for task in r)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_user_info_csv(sys.argv[1])
