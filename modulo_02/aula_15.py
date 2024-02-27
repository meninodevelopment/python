#Generator expression

import sys

# lista = [n for n in range(100000000)] #todos esses dados é armazenado na memoria do computador, quando são muitos dados TRAVA
generator = (n for n in range(10000000)) #esses dados não estão salvos na memoria, ou seja não trava. Mesmo assim ele "sabe" de todos esses valores)

print(generator)
print(sys.getsizeof(generator)) #tamanho do generator

