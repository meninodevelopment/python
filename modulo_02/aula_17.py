try:
    numero_input = 'd'
    numero_int = int(numero_input)
except ValueError as error: #posso definir qual tipo de erro eu espero. Também posso pegar esse erro e "armazenar em uma variavel"
    print('Erro: valor inválido')
    print('Mensagem de erro: ', error)
    print('Nome do erro: ', error.__class__.__name__)