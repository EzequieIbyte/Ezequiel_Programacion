año = int(input("Ingresar el año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El {año} es Bisiesto")

else:
    print(f"El año {año} no es Bisiesto")