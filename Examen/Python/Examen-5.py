def filtrar(lista_palabra, lista_longitud):
    
    return [palabra for palabra in lista_palabra if len(palabra) > lista_longitud]

palabras = ["Pez", "Gato", "Delfin", "Edificio", "Matematicas"]

longitud = 4

palabras_filtrar = filtrar(palabras, longitud)

print(f"Lista: {palabras}")

print(f"Palabras con mas de {longitud} son: {palabras_filtrar}")