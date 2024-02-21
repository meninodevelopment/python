#parte um

valor_input = input('Digite um número inteiro: ')

try:
    if int(valor_input) % 2 == 0:
        print('O valor digitado é par!')
    else:
        print('O valor digitado é ímpar!')
except:
    print('Dado inválido, só é permitido valores númericos inteiros.')

#parte dois
    
horario_input = input('Qual a hora atual? ')

try:
    int_horario_input = int(horario_input)
    if int_horario_input < 12:
        print('Bom dia!')
    elif int_horario_input < 18:
        print('Boa tarde!')
    elif int_horario_input < 24:
        print('Boa noite!')

except:
    print('Dado inválido, só é permitido valores númericos inteiros.')

#parte 3
    
nome_input = input('Digite seu nome: ')
tamanho_nome_input = len(nome_input)

if tamanho_nome_input < 2:
    print('Seu nome ainda é maior que meu pau :(')
elif tamanho_nome_input < 5:
    print(f'Seu nome é curto! Tem {tamanho_nome_input} letras.')
elif tamanho_nome_input < 7:
    print(f'Seu nome é normal! Tem {tamanho_nome_input} letras.')
else:
    print(f'Seu nome é grande! Tem {tamanho_nome_input} letras.')
