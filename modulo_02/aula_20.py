def externa(nome):
    def interna(msg):
        return f'{nome}: {msg}'

    return interna

falas_fabio = externa('Fabio')

print(falas_fabio('Bom dia!'))