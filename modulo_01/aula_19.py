#split -> divide uma string de acordo com o parametro passado ( transforma em uma lista )
#join -> junta uma string

nome = 'Adilan Williams da Silva Lima.'
nome_lista = nome.split() #por padrão o parametro é o ' ' espaço
nome_tupla = tuple(nome.split())
#print(nome_tupla)

pequeno_texto = 'Me chamo Adilan, sou um programador'
pequeno_texto_lista = pequeno_texto.split(',')
#print(pequeno_texto_lista)

#for i, frase in enumerate(pequeno_texto_lista):
    #strip -> corta os ' ' espaços do inicio e do fim
    #rstrip -> corta os ' ' espaços da direita (r: right)
    #lstrip -> corta os ' ' espaços da esquerda (l: left)
    #print(frase.strip())

aluno_nome = 'Marcos Henrique de Souza.'
aluno_nome_tupla = tuple(aluno_nome.split())

for i, nome in enumerate(aluno_nome_tupla):
    print(i, nome)

aluno_nome_junto = '_'.join(aluno_nome_tupla)
print(f'\n{aluno_nome_junto}')

