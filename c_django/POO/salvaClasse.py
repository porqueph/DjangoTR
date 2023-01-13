import json
CAMINHO_ARQUIVO = 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 22)
p3 = Pessoa('Maria', 18)

bd = [vars(p1),vars(p2),vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd,arquivo, ensure_ascii=False, indent=2)