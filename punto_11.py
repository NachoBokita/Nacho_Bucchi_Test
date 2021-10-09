from funciones import suma, resta, division, multiplicacion, pares_e_impares, acumulador


menu = ("""    Menú
        1- suma
        2- resta
        3- division
        4- multiplicacion
        5- pares e impares 
        6- acumulador
        """)

print(menu)

opcion_ingresada = int(input("Ingrese una opción del 1 al 6: "))


if(opcion_ingresada == 1 or opcion_ingresada == 2 or opcion_ingresada == 3 or opcion_ingresada == 4):
    valor_1 = float(input("Ingrese el primer valor: "))
    valor_2 = float(input("Ingrese el segundo valor: "))
    if (opcion_ingresada == 1):
        suma(valor_1, valor_2 )
    elif (opcion_ingresada == 2):
        resta(valor_1, valor_2 )
    elif (opcion_ingresada == 3):
        division(valor_1, valor_2 ) 
    elif (opcion_ingresada == 4):
        multiplicacion(valor_1, valor_2 )      
elif (opcion_ingresada == 5):
    pares_e_impares()
elif (opcion_ingresada == 6):
    acumulador() 
else:
    print("Ingrese un valor válido.")                           

