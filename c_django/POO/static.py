class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi')
        print(args, kwargs)

c1 = Classe()

c1.funcao_que_esta_na_classe(1,2,3)

Classe.funcao_que_esta_na_classe(nomeado = 1)