import math 
print("Semana No. 12 Ejercicio 1")

print("Menú", "a. Sumatoria", "b. Factorial", "c. Tablas de Multiplicar", "d. Número perfecto", sep= "\n")

option= input("Ingrese su opcion: ")

match option:
    case "a":
        n= int(input("Ingrese un numero entero positivo: "))

        if(n<= 0):
            print("Error, Ingrese un numero entero positivo: ")
        else:

            sumatoria = 0
            for contador in range(1, n+1):
                sumatoria += contador

                print(f"La sumatoria es: {sumatoria}")

    case "b":
        n2 = int(input("Ingrese un numero entero postivo: "))
        if n2<= 0:
            print("Error, ingrese un numero postivo")
        else:
            #factorial = math.factorial
            factorial = 1
            for i in range (1, n2+1):
                factorial *= i
                print("El numero factorial es", factorial)

    case "c":
        titulocol = "\t"
        #Imprimir titulo columnas
        for col in range(1, 11):
            titulocol += str(col) + "\t"

        print(titulocol)

        #Imprimir titulo filas
        textofila = ""
        for fila in range(1, 11):
            textofila = str(fila) + "\t"
            
            for col in range(1, 11):
                textofila += str(fila*col) + "\t"
            
            print(textofila)

    case "d":
       numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("Por favor, ingrese un número entero positivo")
else:
    suma = 1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            suma += i
            if i != numero // i:
                suma += numero // i

    if suma == numero:
        print(f"{numero} es un número perfecto")
    else:
        print(f"{numero} no es un número perfecto")
