
class Integer:

    def __init__(self, value = 0):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'Integer: {self.value}'

    def __add__(self, other):
        if not isinstance(other, Integer):
            return NotImplemented
        return Integer(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, Integer):
            return NotImplemented
        return Integer(self.value - other.value)

    
v1 = Integer()
v2 = Integer(5)



    
