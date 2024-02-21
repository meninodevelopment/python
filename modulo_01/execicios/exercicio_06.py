print('Calculadora com Python (Usando Terminal)')
print('-' * 40)

numero_01 = input('Digite o primeiro número: ')
operacao = input('Digite a operação (símbolos): ')
numero_02 = input('Digite o segundo número: ')


try:
    numero_01_float = float(numero_01)
    numero_02_float = float(numero_02)
    resultado = ...

    if operacao == '/':
        resultado = numero_01_float / numero_02_float
    elif operacao == '*':
        resultado = numero_01_float * numero_02_float
    elif operacao == '+':
        resultado = numero_01_float + numero_02_float
    elif operacao == '-':
        resultado = numero_01_float - numero_02_float

    print('-' * 40)
    print(f'O resultado é: {resultado:.2f}')
except:
    print('Dados inválidos, só é permitido números.')

