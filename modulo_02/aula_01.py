def apresentacao(nome, sobrenome=None): #posso colocar um valor padrão
    if sobrenome is None:
        print(f'Bom dia, {nome}')
    else:
        print(f'Bom dia, {nome} {sobrenome}')

apresentacao(sobrenome='Williams', nome='Adilan')