#!/usr/bin/python3
"""Gather data from an API."""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": user_id}
    ).json()

    completed = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"),
            len(completed),
            len(todos)
        )
    )

    for task in completed:
        print("\t {}".format(task.get("title")))
