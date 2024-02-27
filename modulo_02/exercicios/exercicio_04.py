import copy

from modulos import produtos

def aplica_desconto(preco, desconto):
    return round(preco * (1 - (desconto / 100)), 2)

def imprime(msg, lista):
    print(msg)
    for item in lista:
        print(item)

    print()

novos_produtos = copy.deepcopy(produtos)

desconto = 10
produtos_com_desconto = [{**produto, 'preco': aplica_desconto(produto['preco'], desconto)} for produto in novos_produtos]
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos_com_desconto), key=lambda produto: produto['nome'])
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos_com_desconto), key=lambda produto: produto['preco'])
produtos_ordenados_por_nome[3]['preco'] = 1000

imprime('Produtos com desconto:', produtos_com_desconto)
imprime('Produtos ordenados por nome:', produtos_ordenados_por_nome)
imprime('Produtos ordenados por preco:', produtos_ordenados_por_preco)