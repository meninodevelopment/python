#funções decoradoras

def cria_funcao(func):
    def interna(*args, **kwargs):
        print('funcao decoradora...')
        for arg in args:
            e_string(arg)
        return func(*args)
    
    return interna

@cria_funcao #sintax sugar
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma "string".')
    
    return False

invertida = inverte_string('123')

print(invertida)