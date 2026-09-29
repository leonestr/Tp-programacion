
import random

caracteres = ["A", "B", "C", "D", "E", "0", "7"]

caracteres_aleatorios = []

puntaje = 100 

apuesta = 10

opcion = None

puntos_apuesta = 0

mensaje_esperar = "Ingresá enter para continuar..."

mensaje_principal = '''
1. JUGAR
2. CAMBIAR APUESTA
3. SALIR

Elegí una opción: '''

##################################################################################

while puntaje > 0:
    print(f"valor de apuesta: {apuesta}")
    opcion = input(mensaje_principal)
    
    match opcion:
        case "1":
            caracteres_aleatorios = []

            for i in range(3):

                indice_random = random.randint(0, len(caracteres) - 1)
                caracteres_aleatorios.append(caracteres[indice_random])

            print(caracteres_aleatorios)

            if caracteres_aleatorios[0] == "7" and caracteres_aleatorios[1] == "7" and caracteres_aleatorios[2] == "7":
                
                puntaje += (apuesta*10)
                print(f"usted gano: {apuesta*10} puntos, tiene {puntaje}")

            elif caracteres_aleatorios[0] == "0" and caracteres_aleatorios[1] == "0" and caracteres_aleatorios[2] == "0":
                
                puntaje -= puntaje 
                print("USTED PERDIO. su puntaje es 0. Hasta la proxima.")

            elif caracteres_aleatorios[0] == caracteres_aleatorios[1] and caracteres_aleatorios[1] == caracteres_aleatorios[2]:
                
                puntaje += (apuesta*5)
                print(f"usted gano: {apuesta*5} puntos, tiene {puntaje}")

            elif caracteres_aleatorios[0] == caracteres_aleatorios[1] or caracteres_aleatorios[0] == caracteres_aleatorios[2] or caracteres_aleatorios[1] == caracteres_aleatorios[2]:
                
                puntaje += (apuesta*2)
                print(f"usted gano: {apuesta*2} puntos, tiene {puntaje}")

            else:
                
                puntaje -= apuesta
                print(f"PERDIO. -{apuesta} puntos, ahora tiene {puntaje} puntos")
            
        case "2":
            print(f"su saldo es de: {puntaje}")
            
            cambio_apuesta = int(input("¿cuantos puntos desea apostar?"))
            if cambio_apuesta <= 0 or cambio_apuesta > puntaje:
                print("no puede apostar mas puntos de los que tenes o puntos negativos: ")
                cambio_apuesta = int(input("¿cuantos puntos desea apostar?: "))
            else:
                apuesta = cambio_apuesta


        case "3":
            print("SALIO DEL JUEGO")
            print(F"SALDO FINAL:")
            print(puntaje)
            break
        case _:
            print("Opción inválida.")

    input(mensaje_esperar)

    






print("Programa finalizado.")