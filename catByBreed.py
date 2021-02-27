import requests
import pprint
import webbrowser

params = {
    'limit' : 3,
    'breed_ids' : 'acur'
    }

response = requests.get('https://api.thecatapi.com/v1/images/search/', params)

cats = response.json()
for cat in cats:
    webbrowser.open_new_tab(cat['url'])
