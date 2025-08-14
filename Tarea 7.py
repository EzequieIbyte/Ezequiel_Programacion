edad = int(input("Ingrese su edad: "))
lista = input("¿Está en la lista de invitados? (si/no): ") == 'si'

if edad >= 18 and lista:
    print("Acceso permitido")

elif edad < 18 and lista:
    print("Acceso denegado. Debe ser mayor de edad y estar en la lista de invitados.")

else:
    print("Error,vuelva a intentarlo")