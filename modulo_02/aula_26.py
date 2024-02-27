# w -> escrita
# x -> criação
# a -> escreve ao final
# t -> modo text
# b -> binario
# r -> leitura
# + -> leitura e ecrita

# os.remove e os.unlink -> remove arquivo (exclui)
# os.rename -> renomea ou muda o caminho de um arquivo

caminho = 'E:\\code\\python\\modulo_02\\aula_26_pasta\\nomes.txt'

# alunos = [
#     {'nome': 'Anna', 'nota': 7},
#     {'nome': 'Biel', 'nota': 6},
#     {'nome': 'Will', 'nota': 5.5},
# ]

nomes = ['Anna', 'Joao', 'Marcos', 'Julia']

# with open(caminho, 'w+') as arquivo:
#     arquivo.write('Alguma coisa aqui! \r\n')
#     arquivo.write('Com essa função eu posso escrever qualquer coisa no arquivo!')
#     arquivo.seek(0, 0)
#     print(arquivo.read())


with open(caminho, 'w+') as arquivo:
    for i, nome in enumerate(nomes, start=1):
        arquivo.write(f'Nome 0{i}: {nome} \r\n')

    arquivo.seek(0, 0)

with open(caminho, 'r') as arquivo:
    print(arquivo.read().strip())