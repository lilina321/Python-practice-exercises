import random
'''
Program symulujący rzut monetą'''

moneta = ['orzeł', 'reszka']

while True:
    rzut = input('Czy chcesz rzucić monetą? Y/N:')
    if rzut.upper() == 'Y':
        print(random.choice(moneta))
    else:
        print('Nie rzucasz.')

