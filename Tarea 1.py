#Calcula el total a pagar en un restaurante, incluyendo una propina del 15%.

pagar = float(input("Agregue el total a pagar: "))

propina = pagar * 0.15

total = propina + pagar

print(f"La cuenta total es:{total}")

