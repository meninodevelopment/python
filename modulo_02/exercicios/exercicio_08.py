import os

lista = []
itens_removidos = []

while True:
    print('Comandos: [l]istar [d]esfazer [r]efazer [s]air: ')
    req = input('Digite uma tareda ou um comando: ').lower()
    print()


    os.system('cls')
    if req == 'l':
        if not lista:
            print('Você não tem nenhuma tarefa para ser listada.', end='\n\n')
            continue

        print('Tarefas: ', end='\n\n')
        print(*lista, sep='\n', end='\n\n')
    
    elif req == 'd':
        if not lista:
            print('Você não tem nenhuma tarefa para ser removida.', end='\n\n')
            continue

        removido = lista.pop()
        itens_removidos.append(removido)
        print('Removido a tarefa: ', removido)

    elif req == 'r':
        if not lista or not itens_removidos:
            print('Você não tem nenhuma tarefa para ser refeita.', end='\n\n')
            continue

        adicionado = itens_removidos[0]
        lista.append(adicionado)
        print(f'Adicionado a tarefa: "{adicionado}"')
        del itens_removidos[0]

    elif req == 's':
        break
    # print('aqui', req)
    else:
        if len(req) <= 1:
            print('Tarefa inválida', end='\n\n')
            continue

        print(f'Adicionado a tarefa: "{req}"', end='\n\n')
        lista.append(req)
        