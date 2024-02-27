#List Comprehension - filter
import pprint

def p(intervel):
    pprint.pprint(intervel, sort_dicts=False, width=40)

lista = [
    n for n in range(10)#laço for 
    if n % 2 == 0       #condição
    ]

alunos = [
    {'nome': 'Guilherme', 'media': 7.8},
    {'nome': 'Anna', 'media': 5.6},
    {'nome': 'João', 'media': 1.2},
    {'nome': 'Julia', 'media': 10},
]

# print(lista)

alunos_reprovados = [aluno for aluno in alunos if aluno['media'] <= 6.0]
alunos_aprovados = [aluno for aluno in alunos if aluno['media'] >= 6.0]

p(alunos_reprovados)
print()
p(alunos_aprovados)