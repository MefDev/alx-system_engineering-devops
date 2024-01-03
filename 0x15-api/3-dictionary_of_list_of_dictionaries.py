#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a all employee IDs, export the records to JSON.
"""


def gather_all_data():
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url_tasks).json()
    data_json = {}

    for obj in tasks:
        user = data_json.get(obj.get("userId"))
        if user:
            user.append(
                {"task": obj.get('title'), "completed": obj.get(
                    'completed'), "username": user[0]["username"]})
        else:
            data = []
            url_name = "https://jsonplaceholder.typicode.com/users/{}".format(
                int(obj.get("userId")))
            username = requests.get(url_name).json().get("username")
            data.append(
                {"task": obj.get('title'), "completed": obj.get(
                    'completed'), "username": username})
            data_json[obj.get("userId")] = data
    json_file = "todo_all_employees.json"
    with open(json_file, mode='w', newline='') as file:
        json.dump(data_json, file)


if __name__ == "__main__":
    import json
    import requests
    gather_all_data()
