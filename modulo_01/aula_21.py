#operador ternário: <valor> if <condição> else <valor>

nome_input = input('Digite seu nome: ')

print(f'Bom dia, {nome_input.capitalize()}' if nome_input else 'campo vazio :(')