'''
*args

**kwargs - do słowników
'''

def sample(*args):
    print(len(args))
    print(args)

sample(3)
sample(3, 'Ala', 5, 6)

def stick(*components):
    result = ''
    
    for component in components:
        result += str(component)
    return result

print(stick(1, 2, 3, 4))

def sample2(**kwargs):
    print(len(kwargs))
    print(kwargs)

sample2(var1 = 'Python', var2 = ' 3,8')

def func(**kwargs):
    for item in kwargs.items():
        print(item)

func(name = 'John', surname = 'Doe')

def sumInt(**kwargs):
    if kwargs:
        result = 0
        for kwarg in kwargs.values():
            if isinstance(kwarg, int):
                result += kwarg

        return result
    return None

print(sumInt())
print(sumInt(num1 = 40, num2 = 60, num3 = 5.5))


def sample3(*args, **kwargs):
    print(args)
    print(kwargs)

sample3(1, 2, 3, num1 = 6, num2 = 7)


stock = {'name' : 'John', 'surname' : 'Doe'}
numbers = (1, 2, 3)
sample3(*numbers, **stock)
    
