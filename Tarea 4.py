#Pide al usuario su año de nacimiento y di si es mayor de edad.

fecha = int(input("Ingresar año de nacimiento: "))

edad = 2025 - fecha

mayor = (edad >= 18)

if mayor:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")