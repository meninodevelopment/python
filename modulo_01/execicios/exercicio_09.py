import os

lista_de_compras = []

while True:
    print('Selecione uma opção')
    resposta = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    os.system('cls')
    if resposta.isdigit():
        print('Opção inválida.')
        continue

    if resposta == 'i':
        valor = input('Qual o valor? ')
        lista_de_compras.append(valor)
        continue
    
    elif resposta == 'l':
        if not lista_de_compras:
            print('Nada para ser listado.')
            continue
        
        for indice, valor in enumerate(lista_de_compras):
            print(indice, valor)
            continue

    elif resposta == 'a':
        if not lista_de_compras:
            print('Nada para ser apagado.')
            continue

        indice_input = input('Escolha um indice: ')

        if not indice_input.isdigit():
            print('Só é permitido números inteiros.')
            continue

        indice_input_int = int(indice_input)

        if indice_input_int >= len(lista_de_compras):
            print('Não foi possível apagar esse indice')
            continue
            
        del lista_de_compras[indice_input_int]
        continue

    elif resposta == 's':
        break

    else:
        print('Opção inválida')






