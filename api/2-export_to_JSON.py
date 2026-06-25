
rt employee data to JSON
"""

import json
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

                                                    username = user.get("username")

                                                        task_list = []

                                                            for task in todos:
                                                                    task_list.append({
                                                                                "task": task.get("title"),
                                                                                            "completed": task.get("completed"),
                                                                                                        "username": username
                                                                                                                })

                                                                                                                    data = {str(user_id): task_list}

                                                                                                                        with open("{}.json".format(user_id), "w") as file:
                                                                                                                                json.dump(data, file)
