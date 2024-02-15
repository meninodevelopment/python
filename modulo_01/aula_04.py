nome = "Anna"

#repetir_cinco_vezes = nome + "\n" * 5 # da erro
repetir_cinco_vezes = str(nome + "\n") * 5
repetir_cinco_vezes = (nome + "\n") * 5
repetir_cinco_vezes = (nome + " ") * 5

print(repetir_cinco_vezes)