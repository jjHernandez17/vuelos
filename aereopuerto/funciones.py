

def seguir_preguntando (precio_vuelo):
    equipaje_grande = input("Lleva equipaje pesado? (si/no)" )
    if equipaje_grande == "si":
        peso_equipaje_grande = float(input("Ingrese el peso del equipaje grande (kg)"))
        if peso_equipaje_grande <= 20:
            precio_vuelo = precio_vuelo + 50000
        elif peso_equipaje_grande > 20 and peso_equipaje_grande <= 30:
            precio_vuelo = precio_vuelo + 70000
        elif peso_equipaje_grande > 30 and peso_equipaje_grande <= 50 :
            precio_vuelo = precio_vuelo + 110000
        print(f"El costo total de sus maletas mas su boleto es: ${precio_vuelo}")
    elif equipaje_grande == "no":
        print("")
        return precio_vuelo