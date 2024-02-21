alunos = ['joao', 'anna', 'adilan']

for aluno in alunos:
    print(aluno, end=' ')

print()
print(*alunos) #faz a mesma coisa que o laço "for" anterior

matriz = [[123], [456], [789]]

print(*matriz, sep='\n')
