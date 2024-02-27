#variaveis livres

def fora(x):
    a = x
    def dentro():
        return a
    
    return dentro

dentr0_1 = fora(10)
dentr0_2 = fora(20)

# print(dentr0_1())
# print(dentr0_2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar

        return valor_final
    
    return interna

c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))