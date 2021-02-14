'''
pip - pip installs packages - instalator pakunków

PyPi - Python Package Index - indeks (spis) pakunków

'''

import requests

sites = ['http://google.com', 'http://google.com/fddgdg', 'http://allegro.pl']

response = requests.get('http://google.com')

def isExist(site):
    site = requests.get(site)
    if site.status_code == 200:
        return True
    else:
        return False


for site in sites:
    print(isExist(site))


#########################################################

with open('sites.txt') as file:
    tabSites = file.read().splitlines()

 
def isExist(site):
      
        site = requests.get(site)
        if site.status_code == 200:
            return True
        else:
            return False
        
for site in tabSites: 
    print(isExist(site))


