con = input("A quien desea contactar: ")

dic = {
    "Carlos": "04123344545",
    "Eren": "0414322654"} 

if con == "Carlos":
    print(f"El numero es:", dic["Carlos"])

elif con == "Eren":
    print(f"El numero es:", dic["Eren"])

else:
    print("Contacto no encontrado")