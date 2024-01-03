#!/usr/bin/python3
"""
    Python script that, using this REST API,
    for a given employee ID, export the records to JSON.
"""


def gather_data(id, user_todos, current_user):
    """Gather data from an external API"""
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
            current_infos['completed'].append(
                str(todo.get('completed')).lower())
            current_infos['title'].append(todo.get('title'))
    return current_infos


def export_to_json(current_infos, id):
    """Export to JSON"""
    with open('{}.json'.format(id), 'w') as jsonfile:
        jsonfile.write('{')
        jsonfile.write('"{}": ['.format(id))
        for i in range(len(current_infos['title'])):
            jsonfile.write('{')
            jsonfile.write('"task": "{}", "completed": {}, "username": "{}"'
                           .format(current_infos['title'][i],
                                   current_infos['completed'][i],
                                   current_infos['username'][i]))
            if i == len(current_infos['title']) - 1:
                jsonfile.write('}')
            else:
                jsonfile.write('},')
        jsonfile.write(']}')


if __name__ == "__main__":
    import requests
    import sys
    id = int(sys.argv[1])
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
    user_todos = user_todos.json()
    current_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))

    data = gather_data(id, user_todos, current_user)
    export_to_json(data, id)
