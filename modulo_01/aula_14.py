numero_maximo = 10
numero_atual = 0

while numero_atual < numero_maximo:
    numero_atual += 1
    if numero_atual % 2 == 0:
        continue #continue PULA aquela interação do laço

    if numero_atual == 7:
        break #break PARA o laço

    print(f'O numero atual e {numero_atual}')


print('Acabou!!')

x = 0
y = 0

tamanho_maximo = 5

while y < tamanho_maximo:
    while x < tamanho_maximo:
        print(f'{x=} {y=}', end="  ")
        x += 1

    print("")
    y += 1
    x = 0