def suma(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)
    
def resta(numero1, numero2):
    resultado = numero1 - numero2
    print(resultado)    
    
def division(numero1, numero2):
    try:
        resultado = numero1 / numero2
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    print(resultado)  
    
def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    print(resultado)  
    
def pares_e_impares():
    print("ingrese 10 numeros: ")
    i = 0
    numeros = []
    pares = []
    impares = []

    while i < 10:
        input()
        numeros.append(i)
        i = i + 1
    for i in numeros:    
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i)    
    print("Lista de pares: ", pares)
    print("Lista de impares: ", impares)  
    
def acumulador():
    i = 0
    numeros = []
    print("Ingrese 6 números enteros: ")
    while i < 6:
        variable = int(input())
        if (variable <= 0):
            print("El numero ingresado es menor a 0, vuelva a intentarlo.")
            break
        else:  
            numeros.append(variable)  
        i += 1
    print("Numeros ingresados: ", numeros)    
    
               