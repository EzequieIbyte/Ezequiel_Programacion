print("Trate d adivinar un numero del 1 hasta el 30")

while True:

    num = int(input("Coloque un número: "))
    
    if num == 14:
        print("Felicidades has Ganado")
        break

    elif num >= 10 and num <= 13:
        print("Estas muy cerca")

    elif num >= 15 and num <= 16:
        print("UFFF estas muy cerca")

    elif num > 16 and num <= 30:
        print("Estas muy lejos")

    elif num < 10:
        print("Estas muy lejos")

    else:
        ("Estas Frio como el corazon de tu ex")

    