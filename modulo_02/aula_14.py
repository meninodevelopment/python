#dir -> mostra todos os atributos da classe
#hasattr -> checa se determinado metodo existe dentro da classe
#getattr -> executa determinado metodo da classe

string = 'Hello, world!'
metodo = 'upper'

if hasattr(string, metodo):
    print('Esse metodo existe')
    print(getattr(string, metodo))
    print(getattr(string, metodo)())