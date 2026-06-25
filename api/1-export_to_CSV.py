
rt employee data to CSV
"""

import csv
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

                                                        with open("{}.csv".format(user_id), "w", newline="") as file:
                                                                writer = csv.writer(file, quoting=csv.QUOTE_ALL)

                                                                        for task in todos:
                                                                                    writer.writerow([
                                                                                                    user_id,
                                                                                                                    username,
                                                                                                                                    task.get("completed"),
                                                                                                                                                    task.get("title")
                                                                                                                                                                ])
