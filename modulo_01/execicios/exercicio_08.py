import os

palavra_secreta = "broderagem"
palavra_formatada = ''
palavra_formatada_atual = ''
letras_acertadas = ''
tentativas = 0

while True:
    tentativas += 1
    letra = input('Digite uma letra: ').lower()
    

    if not letra:
        print('Você tem que digitar uma letra.')
        continue

    if letra.isdigit():
        print('Digite apenas letras.')
        continue

    if len(letra) > 1:
        print('Digite apenas uma letra por vez.')
        continue
    
    palavra_formatada = ''
    if letra in palavra_secreta:
        letras_acertadas += letra

    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formatada += i
        else:
            palavra_formatada += '*'  
            
    print(palavra_formatada)
    if palavra_formatada == palavra_secreta:
        os.system('cls')
        letras_acertadas = ''
        tentativas = 0
        print(f'Parabéns você ganhou! Com {tentativas} tentativas')

   
    
    