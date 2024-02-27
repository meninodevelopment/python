import json

caminho = 'E:\\code\\python\\pasta_arquivos\\aula_27\\alunos.json'

alunos = [
    {'nome': 'Anna', 'nota': 7},
    {'nome': 'Biel', 'nota': 6},
    {'nome': 'Will', 'nota': 5.5},
]

with open(caminho, 'w') as arquivo:
    json.dump(alunos, arquivo, indent=2)

with open(caminho, 'w') as arquivo:
    pessoa_json = json.load(arquivo) #salva o arquivo dentro da variavel