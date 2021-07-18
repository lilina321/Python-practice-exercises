class Cat:

    def __init__(self, name, favToy, hateToy):
        self.name = name
        self.favToy = favToy
        self.hateToy = hateToy

    def sayHello(self):
        print(f'Hello, my name is {self.name}.')

    def toys(self):
        print(f'My favorite toys: {self.favToy}, my hated toys: {self.hateToy}.')

    def newLikedToy(self, newToy):
        self.newToy = newToy
        if self.newToy not in self.favToy:
            self.favToy.append(self.newToy)
        else:
            print('This toy is already saved.')

    def newDislikedToy(self, newDisToy):
        self.newDisToy = newDisToy
        if self.newDisToy in self.favToy:
            self.favToy.remove(self.newDisToy)
            self.hateToy.append(self.newDisToy)
        else:
            print('There is not such toy.')
        
cat1 = Cat('Ala', ['ryba', 'piłka'], ['kość'])

