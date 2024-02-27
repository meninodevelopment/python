lista = [
    {'nome': 'Anna', 'sobrenome': 'Rodrigues'},
    {'nome': 'Paulo', 'sobrenome': 'Rodrigues'},
    {'nome': 'Matheus', 'sobrenome': 'Henrique'},
    {'nome': 'Adilan', 'sobrenome': 'Williams'},
]

#função lambda
lista.sort(key=lambda item: item['nome']) #sort -> ordana a lista  usando algum parametro e altera a lista original

lista_ordenada_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])#sorted -> gera outra lista ordenada

for pessoa in lista:
    print(pessoa)

print('\n')

print(*lista, sep='\n')
