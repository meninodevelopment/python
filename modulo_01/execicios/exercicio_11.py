import random
cpf_gerado = ''

for i in range(9):
    cpf_gerado += str(random.randint(0, 9))


total_01 = 0
contator_regressivo_01 = 10

for digito in cpf_gerado:
    total_01 += int(digito) * contator_regressivo_01
    contator_regressivo_01 -= 1
digito_01 = (total_01 * 10) % 11
digito_01 = digito_01 if digito_01 < 10 else 0


total_02 = 0
contator_regressivo_02 = 11

for digito in cpf_gerado + str(digito_01):
    total_02 += int(digito) * contator_regressivo_02
    contator_regressivo_02 -= 1
digito_02 = (total_02 * 10) % 11
digito_02 = digito_02 if digito_02 < 10 else 0



cpf_gerado = f'{cpf_gerado}{digito_01}{digito_02}'

print(cpf_gerado)

