import copy

pessoa = {
    'nome': 'Henrique',
    'idade': 46,
}
print(pessoa.__len__(), len(pessoa)) #len -> retorna a quantidade de chaves
print(tuple(pessoa.keys())) #keys -> retorna as chaves
print(list(pessoa.values())) #values -> retorna os valores
print(list(pessoa.items())) #items -> retorna a chave e o valor, semelhante ao enumarate
print(pessoa.get('idade')) #get -> retorna o valor da chave, caso a chave não exista ele retorna None (ou outro valor escolhido)
print(pessoa.pop('nome')) #pop -> exclui aquela chave com o valor e retorna a valor excluido
print(pessoa.popitem()) #exclui o ultimo valor

pessoa.update({ #update -> atualiza o objeto
    'nome': 'Guilherme',
    'sobrenome': 'Kaio',
    'renda': 1485.65
})
pessoa.update(nome="Fabio", idade=54)
print(pessoa)

pessoa_2 = pessoa.copy() #copy -> copia (de maneira superficial) um objeto para outro
pessoa_3 = copy.deepcopy(pessoa) #deepcopy -> copia (de maneira profunda) um objeto para outro

print(pessoa, pessoa_2, sep='\n')