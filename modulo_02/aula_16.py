#Generator function

def gerador(initial_value=0, max_value=10):
    while True:
        yield initial_value #pausa a execução da função, e só é continuada quando é chamado a função "next"
        initial_value += 1

        if initial_value > max_value:
            return
    

gen = gerador()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)