'''
plik - nazwana lokacja, dane przechowywane na stałe na dysku.

ram - pamięć podręczna, dane przechowywane tymczasowo.

Operacje:
- r - read (czytanie) - domyślny
- w - write (pisanie) - jeśli plik istnieje to go usunie,
                        jeśli nie to go stworzy.
- a - append (dopisywanie)  

'''


file = open('text.txt', 'w')

file.write('sample')
file.write('sample')

file.close()

######################################################
try:
    file = open('text2.txt', 'w')

    file.write('sample')
    print(0/0)                  #error, instrukcje po błędzie się nie wykonają
    file.write('sample')

finally:
    file.close()
    
######################################################

with open('text3.txt', 'w') as file:       #plik automatycznie zostanie zamknięty (nawet z błędem)
    file.write('sample')
    print(0/0)
    file.write('sample')

######################################################

'''
Odczytywanie danych:

read
readline
readlines - zwraca tablicę bez \n
splitlines

oceany.txt

Atlantycki
Spokojny
Indyjski
Południowy
'''

with open('oceany.txt') as file:
    oceany = file.read()

'''Terminal

oceany
'Atlantycki\nSpokojny\nIndyjki\nPoL,udniowy'

print(oceany)
Atlantycki
Spokojny
Indyjski
PoL,udniowy'''

######################################################

with open('oceany.txt') as file:
    oceany = file.read().splitlines() #tablica bez \n

'''
oceany
['Atlantycki', 'Spokojny', 'Indysjki', 'PoL,udniowy']
'''

######################################################

with open('oceany.txt', encoding = 'UTF-8') as file:    #kodowanie znaków - polskie znaki
    oceany = file.readline() #czyta pojedynczą linię
    oceany2 = file.readline() #kolejna linia

    oceany3 = file.readlines() #zwraca wszystkie linię jako tablicę wraz z \n

    for line in file
    print(line)

'''
'Atlantycki'

'Spokojny'

'Indysjki'

'Południowy'
'''
######################################################
'''
Wskaźniki w pliku

tell - mówi, gdzie skończona została ostatnia operacja na pliku

seek - zmienia wskaźnik na miejsce wskazane przez użytkowanika
''''
file.readline()
'''Atlantycki'''

file.tell()
'''24'''

file.seek(0)

file.readline()
'''Atlantycki'''

######################################################
'''
Append- dopisywanie na końcu pliku, nie usuwa pliku jeżeli istnieje
'''

with open('oceany.txt', 'a', encoding = 'UTF-8') as file:
    file.write('Arktyczny')

######################################################

'''
Mnogie tryby

- r+ - do czytania i pisania
file.read file.write
nie stworzy pliku jeżeli go nie ma

- w+ - do pisania i czytania
usunie zawartość istniejącego pliku lub stworzy plik gdy go nie było

- a+ - 'wieczny tryb' dopisywania i przy okazji czytania
dopisuje zawsze na końca, nawet jak przeczytamy linijkę

'''


