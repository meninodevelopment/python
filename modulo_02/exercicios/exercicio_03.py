def encontra_primeiro_duplicado(*args):
    numeros = set()

    for numero in args:
        if numero in numeros:
            return numero
        numeros.add(numero)
    
    return -1
    

lista_de_lista_de_inteiros = [
    [1, 5, 1, 6, 6, 8, 5],
    [4, 5, 8, 9, 47, 50, 1],
    [0, 1, 5, 15, 48, 7, 10],
    [4, 51, 12, 10, 12, -5],
]

for lista in lista_de_lista_de_inteiros:
    print(encontra_primeiro_duplicado(*lista))