nota = float(input("Ingresar Nota: "))

if nota >= 80 and nota <= 100:
    print("A")

elif nota >= 60 and nota <= 79:
    print("B")

elif nota >= 40 and nota <= 59:
    print("C")

elif nota >= 20 and nota <= 39:
    print("D")

elif nota >= 0 and nota <= 19:
    print("F")

else:
    print("Nota invalida") 