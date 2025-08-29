def aplanar(*listas):

    lista_aplanada = []
    for lista in listas:
        lista_aplanada.extend(lista)
    return lista_aplanada


lista_1 = [2, 3, 4]
lista_2 = [5, 6 ,7]

lista_final = aplanar(lista_1, lista_2)

print(f"Listas {lista_1} y {lista_2}")

print(f"lista aplanada {lista_final}")
