
class Pet:
 
    def __init__(self, name, age):
        self._name = name
        self.age = age
 
    @property
    def name(self):
        return self._name
 
    @name.setter
    def name(self, value):
        self._name = value
 
    @property
    def age(self):
        return self._age
 

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            if value > 0:
                self._age = value
            else:
                raise ValueError('The value of age must be a positive integer.')
        else:
            raise TypeError('The value of age must be of type int.')
            
try:
    pet = Pet('Max', 'seven')
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
