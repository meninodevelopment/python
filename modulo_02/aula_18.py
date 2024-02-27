def verifica_se_e_zero(n):
    if n == 0:
        raise ZeroDivisionError('Um dos parametros está inválido por ser zero.')

    return True
    
def verifica_se_e_numerico(n):
    if not isinstance(n, (int, float)):
        raise TypeError('Um dos parametros está inválido por não ser dado numerico.')
    
    return True

def divide(n, d):
    verifica_se_e_zero(d)
    verifica_se_e_numerico(n)
    verifica_se_e_numerico(d)
    return n / d

print(divide('3', 2))