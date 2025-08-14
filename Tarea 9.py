compra = int(input("Ingresar el monto de la compra: "))

if compra >= 50 and compra <= 99:
    m = compra * 0.10

    descuento = compra - m  

    print(f"el monto con el 10% de descuento es:{descuento}")

elif compra >= 100:
    c = compra * 0.20

    descuento = compra - c

    print(f"El monto con el 20% de descuento es:{descuento}")

else:
    ("Error vuelva a intentarlo")
