
def pretty_print(func):

    def wrapper():
        print('=' * 30)
        func()
        print('=' * 30)

    return wrapper

def hello():
    print('Python')

hello = pretty_print(hello)


def pretty_print2(func):

    def wrapper2():
        print('=' * 30)
        func()
        print('=' * 30)

    return wrapper2

@pretty_print
def hello2():
    print('Python')

