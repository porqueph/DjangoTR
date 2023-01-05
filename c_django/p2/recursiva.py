def recursiva(inicio=0, fim=10):
    #contar até o final
    #caso base
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())