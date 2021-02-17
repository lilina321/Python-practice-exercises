import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')

tasks = response.json()

userId = 1
sumCompleted = 0
taskDict = dict()


for i in tasks:
    
    if i['userId'] == userId:
        if i['completed'] == True:
            sumCompleted += 1
        taskDict[userId] = sumCompleted
        
    
    else:
        
        sumCompleted = 0
        userId += 1

print(taskDict)

maxValue = max(taskDict.values())
for userId, tasksCompleted in taskDict.items():
    if maxValue == tasksCompleted:
        print('Best worker:', userId)
