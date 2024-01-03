#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID, export the records to CSV.
"""

if __name__ == "__main__":
    import requests
    import sys
    import csv
    id = int(sys.argv[1])
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
    user_todos = user_todos.json()
    current_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    current_user = current_user.json()
    current_infos = {
    }
    for todo in user_todos:
        if todo.get('userId') == id:
            if current_infos.get('title') is None:
                current_infos['title'] = []
            if current_infos.get("completed") is None:
                current_infos['completed'] = []
            if current_infos.get("username") is None:
                current_infos['username'] = []

            current_infos['username'].append(current_user.get('username'))
            current_infos['completed'].append(todo.get('completed'))
            current_infos['title'].append(todo.get('title'))
    with open('{}.csv'.format(id), 'w') as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for i in range(len(current_infos['title'])):
            writer.writerow({"userId": id,
                             "username": current_infos['username'][i],
                             "completed": current_infos['completed'][i],
                             "title": current_infos['title'][i]})
