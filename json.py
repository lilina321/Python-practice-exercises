'''
JSON - wspólny format danych, przekazywanie danych pomiędzy różnymi językami
'''

import json

#ZAPIS DANYCH

json.dumps(data)        #zapisuje dane do postaci stringowej json
json.dumps(data, ensure_ascii=False)        #by były polskie znaki


json.dump(data, nameOfFile, ensure_ascii=False) #zapisuje dane do pliku w postaci json

with open('sample.json', 'w', encoding='UTF=8') as file:
    json.dump(data, file, ensure_ascii=False)

#dump z ang. zrzucić


#ODCZYT DANYCH

json.loads(jsonString)      #przetwarza jsonString na dane typu Python

decodedData = json.loads(encodedData, encoding='UTF-8')


json.load(filePointer)      #wczytuje json z pliku i zwraca jako wynik dane typu Python

with open('sample.json', encoding='UTF=8') as file:
    wynik = json.load(file)

#ŁADNY ODCZYT I ZAPIS - PRETTY PRINTER
    
encodedData = json.dumps(data, ensure_ascii=False, indent=4) #wcięcie
print(encodedData)


with open('sample.json', 'w', encoding='UTF=8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


with open('sample.json', encoding='UTF=8') as file:
    wynik = json.load(file)

print(json.dumps(wynik, indent=4, ensure_ascii=False)

#albo....

import pprint

with open('sample.json', encoding='UTF=8') as file:
    wynik = json.load(file)

pprint.pprint(wynik)
