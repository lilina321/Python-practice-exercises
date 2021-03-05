class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print('Name:', self.name, '\nAge:', self.age)


user1 = User('Anna', 19)
user2 = User('Elsa', 21)

user1.print_data()