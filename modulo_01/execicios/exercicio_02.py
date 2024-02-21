nome = input('Digite seu nome: ')

if nome:
    print('Seu nome é: ', nome)
    print('Seu nome invertido é: ', nome[::-1])
    if ' ' in nome:
        print("Seu nome contém espaços.")
    else:
        print('Seu nome não contém espaços.')

    print(f'Seu nome tem {len(nome)} letras.')
    print('A primeira letra do seu nome é: ', nome[0])
    print('A última letra do seu nome é: ', nome[-1])
else:
    print('Descupe, você deixou campos vazios.')


