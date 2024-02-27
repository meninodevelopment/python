# def ziper(lista_1, lista_2): #uni as duas listas em uma
#     delta = min(len(lista_1), len(lista_2)) #pega a menor lista
    
#     return [
#         (lista_1[i], lista_2[i])
#         for i in range(delta)
#     ]
   
from itertools import zip_longest


nomes_dos_estados = ['São Paulo', 'Rio de Janeiro', 'Paraiba', 'Bahia', 'Pernambuco']
siglas_dos_estados = ['SP', 'RJ', 'PB', 'BH', 'PE', 'BH']

print(list(zip(siglas_dos_estados, nomes_dos_estados))) #python já tem uma função dessa pronta
print(list(zip_longest(siglas_dos_estados, nomes_dos_estados))) #é a mesma coisa que "zip" mas é usado o tamanho da lista maior