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
    usersWithTopCompletedTasks = get_users_with_top_value(dictOfTasks)
    print('Id of users with top completed tasks:', get_users_with_top_value(dictOfTasks))     

# 1 solution
response = requests.get('https://jsonplaceholder.typicode.com/users')

users = response.json()

for user in users:
    if user['id'] in usersWithTopCompletedTasks:
        print('Name of users with top completed tasks:', user['name'])
        #usersWithTopCompletedTasks.remove()
        

# 2 solution

for userId in usersWithTopCompletedTasks:
    
    response = requests.get('https://jsonplaceholder.typicode.com/users/' + str(userId))
    user = response.json()
    print('Name of users with top completed tasks:', user['name'])
    

# 3 solution

for userId in usersWithTopCompletedTasks:
    
    response = requests.get('https://jsonplaceholder.typicode.com/users/', params = 'id=' + str(userId))
    user = response.json()
    print('Name of users with top completed tasks:', user[0]['name'])

# 4 solution

def change_list_into_conj_of_params(my_list):
    res = ''
    for i in my_list:
        if i != my_list[-1]:
            res = 'id=' + str(i) + '&id='
        else:
            res += str(i)
    return res

print(change_list_into_conj_of_params(usersWithTopCompletedTasks))

response = requests.get('https://jsonplaceholder.typicode.com/users/', params = change_list_into_conj_of_params(usersWithTopCompletedTasks))
users = response.json()
for user in users:
    print('Name of users with top completed tasks:', user['name'])
