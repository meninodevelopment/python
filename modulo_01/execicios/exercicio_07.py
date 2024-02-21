frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'
#Posso presentir o perigo e o caos. E ninguém agora vai me amentrondar. Com a minha mente vou a mil lugares. Imaginação me dar forças pra lutar!
i = 0

letra_maxima = ''
letra_quantidade_maxima = 0

while i < len(frase):
    letra_atual = frase[i]
    letra_quantidade_atual = frase.count(letra_atual)

    if letra_atual != ' ' and letra_quantidade_atual > letra_quantidade_maxima:
        letra_maxima = letra_atual
        letra_quantidade_maxima = letra_quantidade_atual
    
    i += 1
else:
    print(f'A letra que mais apareceu foi "{letra_maxima}", ela apareceu {letra_quantidade_maxima} vezes.')
