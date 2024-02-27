pessoa = {}

#nome = input('Qual é o seu nome? ')
nome = 'João'

#aqui eu posso tratar a variavel "nome" antes de coloca-la na variavel "pessoa"

pessoa['nome'] = nome
pessoa['sobrenome'] = 'Fábio'
pessoa['idade'] = 50


for chave in pessoa:
    print(pessoa[chave])

#print(pessoa['endereco']) isso gera erro

#if not pessoa['endereco']: também gera erro
#   print('Essa chave não existe.')
    
print(pessoa.get('endereco')) #por padrão o valor retornaod é "None"
print(pessoa.get('endereco', 'OOOOOO MAY GOD')) #mas eu posso mudar isso

if pessoa.get('endereco') is None:
    print('Essa chave não existe')