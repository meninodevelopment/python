from itertools import groupby

produtos = [
    {'nome': 'Hamburguer', 'categoria': 'salgado'},
    {'nome': 'Pastel', 'categoria': 'salgado'},
    {'nome': 'Coca-cola', 'categoria': 'bebida'},
    {'nome': 'Bolo', 'categoria': 'doce'},
    {'nome': 'Torta Doce', 'categoria': 'doce'},
    {'nome': 'Suco', 'categoria': 'bebida'},
    {'nome': 'Mousse', 'categoria': 'doce'},
]

def order(produto):
    return produto['categoria']

produtos_ordenados = sorted(produtos, key=order)
produtos_agrupados = groupby(produtos_ordenados, key=order)
# print(*produtos_ordenados, sep='\n')

for categoria, grupo in produtos_agrupados:
    print(categoria)

    for produto in grupo:
        print(produto)
    
    print()