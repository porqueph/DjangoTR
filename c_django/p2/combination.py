from itertools import combinations

pessoas = ['joao','pedro','luiz','leticia']

camisetas = ['preta','branca']


print(*list(combinations(pessoas,2)),sep='\n')