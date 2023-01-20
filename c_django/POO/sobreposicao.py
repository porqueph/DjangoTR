class MinhaString(str):
    def upper(self):
        print('Chamou UPPER')
        return super().upper()



string = MinhaString('pedro')

print(string.upper())