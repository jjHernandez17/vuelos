from funciones import *
import time
vuelos = {}
comprar_otro_boleto = True

while comprar_otro_boleto:
    while True:
        print("---"*30)
        print("Sistema compra boletos de viaje")
        print("---"*30)

        tipo_viaje = input("Ingrese que tipo de boleto desea comprar (nacional/internacional)")
        if tipo_viaje.lower() == "nacional":
            print("Estos son los viajes disponibles nacionales: \n")
            print ("==="*30)
            print("(1)   Bogotà ----> Medellìn        17/ 08 / 2025         $230.000 ")
            print ("==="*30)
            print("")
            print ("==="*30)
            print("(2)   Bogotà ----> Cali            17/ 08 / 2025         $160.000")
            print ("==="*30)
            print("")
            print("")

            viaje = int(input("Ingrese la opcion del boleto que  desea comprar , si quiere cancelar, escriba: cancelar"))
            if viaje == "cancelar":
                print("Cargando...")
                time.sleep(3)
            elif viaje == 1:
                precio_vuelo = 230000
            elif viaje == 2:
                precio_vuelo = 160000
            nombre = input("Ingrese su nombre completo: \n")

            equipaje_mano = input("lleva equipaje_mano de mano? (si/no)")
            if equipaje_mano == "si":
                peso_equi_mano = float(input("Indique el peso del equipaje_mano de mano (kg) \n"))
                if peso_equi_mano > 0 and peso_equi_mano<= 13:
                    print("Equipaje permitido, puede seguir viajando")
                    seguir_preguntando (precio_vuelo)
                else:
                    seguir_viajando = input("Peso del equipaje_mano no aprobado, desea seguir comprando el boleto sin el equipaje_mano? (si,no)\n")
                    if seguir_viajando.lower() == "si":
                        seguir_preguntando (precio_vuelo)
                        
                    elif seguir_viajando.lower() == "no":
                       comprar_otro_boleto = False

                    


    


