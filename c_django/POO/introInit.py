string = 'Pedro'

print(string.upper())


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Pedro', 'Fagundes')
#p1.nome = 'Pedro'
#p1.sobrenome = 'Fagundes'
print(p1)
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa('Query','Apuk')
#p2.nome = 'Query'
#p2.sobrenome = 'Appuk'

print(p2.nome)
print(p2.sobrenome)