import re

while True:
    #cpf_usuario = input('Digite seu CPF: ')
    cpf_usuario = re.sub(r'[^0-9]', '', '07868910410')

    if len(cpf_usuario) != 11:
        print('CPF inválido.')
        break

    if cpf_usuario == (cpf_usuario[0] * 11):
        print('CPF inválido')
        break

    cpf_usuario_nove_primeiros_digitos = cpf_usuario[:9]

    total_01 = 0

    #jeito que eu fiz
    #for i, valor in enumerate(range(10, 1, -1)):
    #    cpf_usuario_numero_atual_int = int(cpf_usuario_nove_primeiros_digitos[i])
    #    total += cpf_usuario_numero_atual_int * valor


    #jeito que o professor fez
    contator_regressivo_01 = 10
    for digito in cpf_usuario_nove_primeiros_digitos:
        total_01 += int(digito) * contator_regressivo_01

        contator_regressivo_01 -= 1

    digito_01 = (total_01 * 10) % 11
    digito_01 = digito_01 if digito_01 < 10 else 0

    print(digito_01)


    total_02 = 0
    contator_regressivo_02 = 11
    for digito in cpf_usuario_nove_primeiros_digitos + str(digito_01):
        total_02 += int(digito) * contator_regressivo_02

        contator_regressivo_02 -= 1

    digito_02 = (total_02 * 10) % 11
    digito_02 = digito_02 if digito_02 < 10 else 0

    print(digito_02)

    cpf_gerado = f'{cpf_usuario_nove_primeiros_digitos}{digito_01}{digito_02}'

    if cpf_gerado == cpf_usuario:
        print(f'O CPF: {cpf_usuario} é válido.')
    else:
        print('CPF inválido.')

    break

    
