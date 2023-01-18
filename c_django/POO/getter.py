# class Caneta:
#     def __init__(self,cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('Get COR')
#         return self.cor_tinta

# caneta = Caneta('Azul')

# print(caneta.get_cor())

# print(caneta.get_cor())

# print(caneta.get_cor())


class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

caneta = Caneta('Azul')

print(caneta.cor)

print(caneta.cor)

print(caneta.cor)