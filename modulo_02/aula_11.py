#List Comprehension
#exemplo 1:
lista = []

for numero in range(10):
    lista.append(numero)

# print(lista)
         
lista = [
    numero #valor retornado
         
    for numero in range(10) #laço for     
]


#exemplo 2
def aplica_desconto(preco_original, desconto):
    return round(preco_original * (1 - (desconto / 100)), 2)

produtos_lista = [
    {'nome': 'Caneta', 'preco': 4.5},
    {'nome': 'Caserno', 'preco': 18.75},
    {'nome': 'Notebook', 'preco': 1985.6},
    {'nome': 'Violão', 'preco': 156.99},
]

desconto = 10
produtos_lista_com_desconto = [
    {**produto, 'preco': aplica_desconto(produto['preco'], desconto)} if produto['preco'] > 50 else {**produto}
    for produto in produtos_lista
]
print(*produtos_lista_com_desconto, sep='\n')

