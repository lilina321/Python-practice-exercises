import random
import string

print('Welcome to password generator')

chars = string.ascii_letters + string.digits + string.punctuation
numberOfPasswords = int(input('Enter number of passwords: '))
passwordLength = int(input('Enter password length: '))

print('Here are your passwords: ')
for i in range(numberOfPasswords):
    password = ''
    for i in range(passwordLength):
        password += random.choice(chars)

    print(password)




