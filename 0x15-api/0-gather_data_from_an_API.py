#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID, returns
    information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys
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
        if todo.get('completed') is True:
            if current_infos.get('done_tasks') is None \
                    or current_infos.get('title') is None:
                current_infos['done_tasks'] = 1
                current_infos['title'] = []
            else:
                current_infos['done_tasks'] += 1
                current_infos['title'].append(todo.get('title'))
        for key, value in current_user.items():
            if key == 'name':
                current_infos['employee_name'] = value
    print("Employee {} is done with tasks({}/{}):".format(
        current_infos.get('employee_name'),
        current_infos.get('done_tasks'), len(user_todos)))
    for title in current_infos.get('title'):
        print("\t {}".format(title))
