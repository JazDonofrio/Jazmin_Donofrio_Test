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


#Si la opcion elegia es una de las primeras cuatro entra en el if y le pide los numeros
if(opcion_elegida == 1 or opcion_elegida == 2 or opcion_elegida == 3 or opcion_elegida == 4):
    
    numero1 = int(input("Ingrese un primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    
    
#Si la opcion ingresada concuerda con algun valor permitido (1, 2, 3, 4), entra en el siguiente if, correspondiente a las funciones
#que se necesiten los dos valores ingresados por el usuario
    if (opcion_elegida == 1):
        suma(numero1, numero2 )
        
    elif (opcion_elegida == 2):
        resta(numero1, numero2 )
        
    elif (opcion_elegida == 3):
        division(numero1, numero2 ) 
        
    elif (opcion_elegida == 4):
        multiplicacion(numero1, numero2 )    
          
elif (opcion_elegida == 5):
     pares_impares()
    
elif (opcion_elegida == 6):
    acumulador() 
    
else:
    print("Ingrese un valor válido.")        