'''
Funkcja generujące w nieskończoność kolejne liczby przemnożone przez siebie
1, 4, 9, 16 ...

Skorzystaj z funkcji generując 20 elementów, po czym wróć do momentu skończenia
i wygeneruj następne 30 kolejnych liczb.

Zapisz wygenerowane elementy w tej samej liście.
'''

def number_multiplied_by_itself():
    x = 0
    while True:
        x += 1
        yield x * x


generatedNumbers = []

a = number_multiplied_by_itself()

for _ in range(20):
    generatedNumbers.append(next(a))

print(generatedNumbers)


for _ in range(30):
    generatedNumbers.append(next(a))

print(generatedNumbers)

#a.send(20) - wysyłanie wartości do generatora
#a.send(None) - uruchomienie generatora
        
