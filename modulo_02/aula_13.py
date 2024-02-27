#matriz com List Comprenhrension

matriz = []

for x in range(3):
    for y in range(3):
        matriz.append((x, y))

matriz = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(matriz)