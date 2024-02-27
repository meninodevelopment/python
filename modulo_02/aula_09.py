conjunto_01 = {1, 5, 8, 7, 5} 
conjunto_02 = {1, 4, 8, 6, 5}

conjunto_03 = conjunto_01 | conjunto_02 #retorna os itens unidos dos set's
conjunto_04 = conjunto_01 & conjunto_02 #retorna os itens presente nos dois set's
conjunto_05 = conjunto_01 - conjunto_02 #retorna os itens presentes no set da esquerda que não esteja presenta no set da direita
conjunto_06 = conjunto_01 ^ conjunto_02 #retorna os itens únicos de cada set

print(conjunto_03)
print(conjunto_04)
print(conjunto_05)
print(conjunto_06)
