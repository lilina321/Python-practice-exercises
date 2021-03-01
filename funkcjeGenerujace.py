'''
yield - z ang. dostarczyć, dać, wydać z siebie
'''

def generate_even_numbers():
    print('start')
    for element in range(400):
        print('przed yield')
        if (element % 2) == 0:
            yield element
            print('po yield')
            
a = generate_even_numbers()

#next(a) - krok po kroku
#możemy powrócić do miejsca wywołania

def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x += 1

print(list(generate_10_numbers()))
print(list(generate_10_numbers()))
print(list(generate_10_numbers()))

# funkcje można wywołać kilkukrotnie, a generator 1 bo potem pusty

generate_10_numbers_expression = (x for x in range(10))

print(list(generate_10_numbers_expression))
print(list(generate_10_numbers_expression))

