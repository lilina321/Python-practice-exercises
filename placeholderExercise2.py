import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')

def count_task_frequency(tasks):
    dictOfTasks = dict()

    for entry in tasks:
        if entry['completed'] == True:
            try:
                dictOfTasks[entry['userId']] += 1
            except KeyError:
                dictOfTasks[entry['userId']] = 1
                
    return dictOfTasks


def get_users_with_top_value(dictOfTasks):
    usersWithTopCompletedTasks = []
    for userId, completedTasks in dictOfTasks.items():
        if max(dictOfTasks.values()) == completedTasks:
            usersWithTopCompletedTasks.append(userId)
    return usersWithTopCompletedTasks


try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print('Invalid format')
else:        
    dictOfTasks = count_task_frequency(tasks)
    print('Id of users with top completed tasks:', get_users_with_top_value(dictOfTasks))     
