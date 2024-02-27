perguntas = [
    {
        'pergunta': 'Quanto é 4 X 5',
        'opcoes': ['20', '25', '16', '15'],
        'resposta': '20'
    },
    {
        'pergunta': 'Quanto é 80 dividido por 20',
        'opcoes': ['2', '6', '4', '10'],
        'resposta': '4'
    },
    {
        'pergunta': 'Qual é a raiz quadrada de 64',
        'opcoes': ['24', '8', '16', '4'],
        'resposta': '8'
    },
]

quantidade_perguntas_acertadas = 0

for pergunta in perguntas:
    print(pergunta['pergunta'])
    print('Opções:')
    
    for opcao, resposta in enumerate(pergunta['opcoes'], 1):
        print(f'{opcao}) {resposta}')
    
    resposta_input = input('Escolha uma opção: ')

    try:
        resposta_input = int(resposta_input)

        if resposta_input > 4 or resposta_input < 1:
            print('Resposta inválida, tente uma das opções ao lado (1, 2, 3, 4)')
            continue
    except:
        print('Resposta inválida, tente uma das opções ao lado (1, 2, 3, 4)')
        continue
    
    if pergunta['resposta'] == pergunta['opcoes'][resposta_input - 1]:
        print('Você acertou, estou orgulhoso de você')
        quantidade_perguntas_acertadas += 1
    else:
        print('Você errou, mas não se preocupe, continue se esforçando!')
    
if quantidade_perguntas_acertadas == 0:
    print('Infelizmente você não conseguiu acertar as perguntas, mas não desista e tente novamente, acredito em você!')
elif quantidade_perguntas_acertadas <= 2:
    print(f'Você acertou {quantidade_perguntas_acertadas} perguntas de {len(perguntas)}, PARABÉNS! Eu sabia que você ia conseguir ')
elif quantidade_perguntas_acertadas == len(perguntas):
    print('VOCÊ ACERTOU TODAS AS PERGUNTAS, PARABÉNS!! VOCÊ É MUITX INTELIGENTE!!')