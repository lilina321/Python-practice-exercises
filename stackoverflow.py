import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

'''
timedelta - czas do odejmowania
time stamp - znak czasu 1 stycznia 1970

'''
timeBefore = timedelta(days = 7)

searchDate = datetime.today() - timeBefore

print(int(searchDate.timestamp()))

'''
API - Application Programming Interface

Inter - pomiędzy
'''

params = {
    'site' : 'stackoverflow',
    'sort' : 'votes',
    'min' : 10,
    'order' : 'desc',
    'tagged' : 'python',
    'fromdate' : int(searchDate.timestamp())
    }

response = requests.get('https://api.stackexchange.com/2.2/questions/', params)

try:
    questions = response.json()
except json.decoder.JSONDecodeError:
    print('Niepoprawny format')
else:
    for question in questions['items']:
        webbrowser.open_new_tab(question['link'])
    
