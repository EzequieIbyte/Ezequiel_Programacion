def matriz_transformada(matriz, numero):
    return [[elemento * numero for elemento in fila] for fila in matriz]

matriz_original = [[1, 2], [3, 4]]
matriz_transformada = matriz_transformada(matriz_original, 3)

print("----------Matriz Original----------")
print(matriz_original)

print("----------Matriz Transformada----------")
print(matriz_transformada)

