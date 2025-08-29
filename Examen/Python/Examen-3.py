def recursivo(lista):
    if not lista:
        return 1
    

    return lista[0] * recursivo(lista[1:])

lista_1 = [2, 3, 4]
print(f"Producto de {lista_1} es: {recursivo(lista_1)}")

