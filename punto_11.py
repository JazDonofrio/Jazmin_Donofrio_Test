from funciones import suma, resta, division, multiplicacion, pares_impares, acumulador

menu = ("""   
        >>> Menú <<<
        
        1-> suma
        2-> resta
        3-> division
        4-> multiplicacion
        5-> pares e impares 
        6-> acumulador
        """)

print(menu)


opcion_elegida = int(input("Ingrese una opción del menu del 1 al 6: "))
print("Opcion elegida: ", opcion_elegida)

while opcion_elegida == 1 or opcion_elegida == 2 or opcion_elegida == 3 or opcion_elegida == 4:
    
#Si la opcion elegia es una de las primeras cuatro entra en el if y le pide los numeros
    numero1 = int(input("Ingrese un primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))

    if (opcion_elegida == 1):
        suma(numero1, numero2 )
        break
    
    elif (opcion_elegida == 2):
        resta(numero1, numero2 )
        break
        
    elif (opcion_elegida == 3):
        division(numero1, numero2 ) 
        break
        
    elif (opcion_elegida == 4):
        multiplicacion(numero1, numero2 )    
        break
        
if (opcion_elegida == 5):
       pares_impares()
    
elif (opcion_elegida == 6):
    acumulador() 
    
else:
    print("Ingrese un valor válido.") 
               