def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
       (l1[i],l2[i]) for i in range(intervalo) 
    ]

l1 = ['salvador', 'ubatuba', 'belo horizonte']
l2 = ['BA','SP','MG','RJ']

print(zipper(l1,l2))

print(list(zip(l1,l2)))

from itertools import zip_longest

print(list(zip_longest(l1,l2, fillvalue='SEM CIDADE')))