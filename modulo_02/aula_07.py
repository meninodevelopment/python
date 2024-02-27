#set -> estrura de dados mutável, mas que só recebe dados imutáveis, além de não ter "ordem" nos valores e nem indice

conjunto = {1, 5, 8, 7, 5, 5, 5, 5} # não aceita valores duplicados, por padrão é excluído
#print(conjunto, type(conjunto))

nomes_lista = ['adilan', 'biel', 'vitor', 'anna', 'biel', 'Adilan']
nomes_set = set() #set vazio

for nome in nomes_lista:
    nomes_set.add(nome.lower())

nomes_lista_sem_repeticao = list(nomes_set)

print(nomes_lista_sem_repeticao)
print(nomes_set)


