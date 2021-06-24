#zad 1
import random

roll = random.randint(1, 6)
print('Drawn number', roll)

#zad 2

word = input('Write a word: ')
print('Hello', word)

#zad 3

numberOfGuests = int(input('Write a number of guests: '))
numberOfCandies = int(input('Write a number of candies: '))

print('The rest of the candies:', numberOfCandies % numberOfGuests)

#zad 4

print('*' * 20)

#zad 5
number = input('Write a number: ')
print('Number has', len(number), 'digits.')

#zad 6
number = input('Write a number: ')
try:
    print('Result:', int(number) * 10)
except ValueError:
    print('Invalid format')

#zad 7
word = input('Write a word: ')
print(word[0])

#zad 8

number = int(input('Write a number: '))
if number % 2 == 0:
    print('Even number.')
elif number % 2 != 0 :
    print('Odd number.')

#zad 9

age = int(input('Enter your age: '))
if age >= 13 and age <= 17:
    print('You are teenager.')
else:
    print('You are not a teenager.')

#zad 10
try:
    number = int(input('Write a number: '))
    if number % 8 == 2:
        print(True)
    else:
        print(False)
except:
    print('Invalid data')
    
# zad 11
word = input('Write a word: ')
if word[0] == 'M':
    print(True)
else:
    print(False)


#zad 12
word = input('Write a word: ')
if 'kot' in word:
    print(True)
else:
    print(False)
    
#zad 13
word = input('Write a word: ')
print(word.upper())

#zad 14
word = input('Write a word: ')
if word == 'Akademia':
    print(True)
else:
    print(False)

#zad 15
word = input('Write a word: ')
if word.lower()[-1] == 'm':
    print(True)
else:
    print(False)

#zad 16
number1 = int(input('Write a number: '))
number2 = int(input('Write a number: '))
if number1 > number2:
    print(number1)
elif number1 == number2:
    print('The numbers are equal.')
else:
    print(number2)

#zad 17
tab = []
for i in range(3):
    number = int(input('Write a number: '))
    tab.append(number)

print(max(tab))

#zad 18
number1 = int(input('Write a number: '))
number2 = int(input('Write a number: '))
print((number1 + number2) / 2)

#zad 19
name = input('Write a name: ')
if name[-1] == 'a' and name != 'Barnaba':
    print('Female name.')
else:
    print('Male name.')

#zad 20
import math
number1 = int(input('Write a number: '))
number2 = int(input('Write a number: '))

print(math.sqrt(number1**2 + number2**2))

#zad 21
number = int(input('Write a number: '))
print(1/number)

#zad 22
import random
print(random.randint(1, 100))

#zad 23
r = int(input('Write a radius: '))
print('Circle field:', 3.14 * (r**2))

#zad 24
word = input('Write a word: ')
print(word[0] == 'A')

#zad 25
word1 = input('Write a word: ')
word2 = input('Write a word: ')
if word1 == word2:
    print('Yes')
else:
    print('No')

#zad 26
word = input('Write a word: ')
if word == word[::-1]:
    print('Yes')
else:
    print('No')

#zad 27
number1 = int(input('Write a number: '))
number2 = int(input('Write a number: '))
print(number1**number2)

#zad 28
word = input('Write a word: ')
print(word[1])

#zad 29
word = input('Write a word: ')
newWord = word.replace('*', '')
print(newWord)

#zad 30
word = input('Write a word: ')
print(word[-3:] == 'tka')

