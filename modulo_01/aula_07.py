primeiro_nome = "Joana"
segundo_nome = "Maria"
terceiro_nome = "Iago"

primeira_media = 8.4578
segunda_media = 7.8456
terceira_media = 5.695

#string = 'aluno_01: {0} media: {3:.2f} \naluno_02: {1} media: {4:.2f} \naluno_03: {2} media: {5:.2f}' posso me refencia a cada argumento pelo index.
#formato = string.format(primeiro_nome, segundo_nome, terceiro_nome, primeira_media, segunda_media, terceira_media)

string = 'aluno_01: {aluno_01} media: {media_01:.2f} \naluno_02: {aluno_02} media: {media_02:.2f} \naluno_03: {aluno_03} media: {media_03:.2f}' # ou eu posso nomar cada argumento com um parametro
formato = string.format(aluno_01=primeiro_nome, aluno_02=segundo_nome, aluno_03=terceiro_nome, media_01=primeira_media, media_02=segunda_media, media_03=terceira_media) 

print(formato)
print(4/2)