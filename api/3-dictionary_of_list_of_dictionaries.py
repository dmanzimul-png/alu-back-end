
rt all employees to JSON
"""

import json
import requests


if __name__ == "__main__":
        users = requests.get(
                "https://jsonplaceholder.typicode.com/users"
                    ).json()

                        todos = requests.get(
                                "https://jsonplaceholder.typicode.com/todos"
                                    ).json()

                                        result = {}

                                            for user in users:
                                                    user_id = str(user.get("id"))
                                                            username = user.get("username")

                                                                    result[user_id] = []

                                                                            for task in todos:
                                                                                        if task.get("userId") == user.get("id"):
                                                                                                        result[user_id].append({
                                                                                                                            "username": username,
                                                                                                                                                "task": task.get("title"),
                                                                                                                                                                    "completed": task.get("completed")
                                                                                                                                                                                    })

                                                                                                                                                                                        with open("todo_all_employees.json", "w") as file:
                                                                                                                                                                                                json.dump(result, file)
