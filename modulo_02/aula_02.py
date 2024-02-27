def somar(*args):
    total = 0
    for numero in args:
        total += numero

    return total

numeros = (1, 2, 3, 4, 5, 6, 7, 8)
#resultado = somar(numeros) -> isso da erro
resultado = somar(*numeros) # -> estou desempacotando e mandando para a função

print(resultado)
print(f'Função sum: {sum(numeros)}') # função pronta do python