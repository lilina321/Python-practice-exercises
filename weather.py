#pypi.org
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

r = requests.get('https://pogoda.onet.pl/prognoza-pogody/wroclaw-362450')

soup = BeautifulSoup(r.content, 'html.parser')
element = soup.find('div', {'class' : 'temp'})
print('Temperature in Wrocław:', element.text)
