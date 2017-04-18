#!/usr/bin/python3
"""
This modules returns the to do list of an employee based on id

This is done with eh CSV format
"""
import csv
import requests
import sys


def get_user_info_csv(user_id):
    url_root = "https://jsonplaceholder.typicode.com"
    url_users = url_root + "/users"
    url_todos = url_root + "/todos"
    name = requests.get("{}/{}".format(url_users, user_id)).json().get("username")
    r = requests.get("{}/?userId={}".format(url_todos, user_id)).json()
    with open("{}.csv".format(user_id), "w", newline="") as f:
        csvwriter = csv.writer(f, delimiter=",", quotechar='"',
                              quoting=csv.QUOTE_ALL)
        csvwriter.writerows([user_id, name, task.get("completed"),
                            task.get("title")] for task in r)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_user_info_csv(sys.argv[1])
