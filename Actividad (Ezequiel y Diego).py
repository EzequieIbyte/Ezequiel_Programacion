def agregar(cesta):
    elemento = input("Introduce el nombre del elememnto a agregar: ")
    precio = float(input("Introduce el precio del elemento: "))
    cesta[elemento] = precio
    print(f"¡{elemento} agregado a la cesta por ${precio:.2f}!")


def mostrar(cesta):
    if not cesta:
        print("La cesta de la compra esta vacia")
    
    else:
        print("\n-----------Elementos de la cesta-----------")
        for elemento,precio in cesta.items():
            print(f"{elemento}:${precio}")
            
def eliminar(cesta):
    elemento = input("Introduce el nombre del elemento a eliminar: ")
    if elemento in cesta:
        del cesta[elemento]
        print(f"¡{elemento} eliminado de la cesta!")
    else:
        print(f"No se encontró {elemento} en la cesta.")


def calcular(cesta):
    total = sum(cesta.values())
    print(f"El total de la compra es:${total}")
    
def menu():
    cesta = {}
    while True:
        print("\n-----------Menu de cesta de compras-----------")

        print("1- Agregar elemento:\n"
              "2- Mostrar el contenido de la cesta:\n"
              "3- Eliminar un elemento:\n"
              "4- Calcular monto:\n"
              "5- Salir:\n")
        
        opcion = int(input("Seleccione 1 opcion(1 - 5): "))

        if opcion == 1:
            agregar(cesta)
        
        elif opcion == 2:
            mostrar(cesta)

        elif opcion == 3:
            eliminar(cesta)

        elif opcion == 4:
            calcular(cesta)

        elif opcion == 5:
            print("Gracias por probar el programa")
            break

        else:
            print("Opcion invalida")
        


menu()


        

