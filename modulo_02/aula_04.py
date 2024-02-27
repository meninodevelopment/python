#dic

pessoa = {
    'nome': 'Anna',
    'sobrenome': 'Caroline',
    'idade': 18
}

print(pessoa['nome'], end='\n\n')

for chave in pessoa: #no laço for é pego a chave e não o valor
    print(chave, pessoa[chave])