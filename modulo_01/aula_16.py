lista_de_compras = ['maça', 'banana', 'arroz', 'macarrão', 'frango']

#del -> deleta um elemento da lista pelo indice
#del lista_de_compras[1]

#pop -> delete o último elemento da lista e retorna esse elemento
#lista_de_compras.pop()

#insert -> adiciona um elemento na lista no indice selecionado 
#lista_de_compras.insert(0, 'goiaba')

#append -> adiciona um elemento no último indice da lista
#lista_de_compras.append('bolacha')

print(lista_de_compras)

#despacotamento

nomes = ['João', 'Marcio', 'Anna']

#nome_1, nome_2, nome_3 = ['João', 'Marcio', 'Anna']
#nome_1, nome_2, nome_3 = nomes

#nome, *resto = nomes
_, nome, *_ = nomes

print(nome)