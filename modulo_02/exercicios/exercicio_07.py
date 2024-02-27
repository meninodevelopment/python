def soma_listas(lista1, lista2):
    return [x + y for x, y in zip(lista1, lista2)]

lista1 = [4, 2, 5, 8, 60, 25, 1000]
lista2 = [4, 1, 0, 5]

print(soma_listas(lista1, lista2))