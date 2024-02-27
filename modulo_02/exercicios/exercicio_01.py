def crair_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    
    return multiplica

duplicar = crair_multiplicador(2)
triplicar = crair_multiplicador(3)

print(duplicar(3))
print(triplicar(3))