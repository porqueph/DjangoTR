string = 'Pedro'

print(string.upper())


class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Pessoa()
p1.nome = 'Pedro'
p1.sobrenome = 'Fagundes'
print(p1)
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Query'
p2.sobrenome = 'Appuk'

print(p2.nome)
print(p2.sobrenome)