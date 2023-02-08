class Ponto:
    def __init__(self, x, y):
      self.x = x
      self.y = y

    def __str__(self):
        return f'{self.x} , {self.y}'
    def __repr__(self):
       class_name = self.__class__.__name__
       return f'{class_name}(x={self.x}, y={self.y})'

p1 = Ponto(1,2)
p2 = Ponto(19,1923)

print(repr(p1))
print(p2)