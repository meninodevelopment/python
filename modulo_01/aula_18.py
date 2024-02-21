#enumerate() -> enumera cada elemento da lista

nomes = ['Anna', 'Maria', 'Marcio']

for nome in enumerate(nomes):
    print(nome)

for indice, valor in enumerate(nomes):
    print(indice, valor)