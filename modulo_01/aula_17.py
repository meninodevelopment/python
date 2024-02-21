#tupla -> lista imutável

nomes = ['Anna', 'Maria', 'Marcio'] # lista mutável


nomes_02 = ('Anna', 'Maria', 'Marcio') # lista imutável. Funciona como uma lista normal, mas não é possivel alterar os dados.
nomes_02 = tuple(nomes)

print(nomes)
print(nomes_02)
