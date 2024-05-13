import random
#Andre Donis 1210624

print("Semana No. 16: Ejercicio 1")

def generarNumeros():
    return [random.randint(1, 100) for _ in range(10)]

def mostrarNumeros(arreglo):
    print("Números ingresados:", arreglo)

def calcularPromedio(arreglo):
    return sum(arreglo) / len(arreglo)

def mostrarPromedio(arreglo):
    print("Promedio del arreglo:", calcularPromedio(arreglo))

def mostrarLongitud(arreglo):
    print("Longitud del arreglo:", len(arreglo))

def sumarPosicionesPares(arreglo):
    suma = sum(arreglo[::2])
    print("Suma de posiciones pares:", suma)

def sumarPosicionesImpares(arreglo):
    suma = sum(arreglo[1::2])
    print("Suma de posiciones impares:", suma)

def main():
    arreglo = generarNumeros()
    
    while True:
        print("\n Por favor, seleccione una opción:")
        print("a. Mostrar los números ingresados")
        print("b. Mostrar el promedio del arreglo")
        print("c. Mostrar la longitud del arreglo")
        print("d. Encontrar y mostrar:")
        print("   i. La suma de posiciones pares")
        print("   ii. La suma de posiciones impares")
        print("q. Salir")
        
        opcion = input("Opción: ").lower()
        
        match opcion:
            case 'a':
                if not arreglo:
                    print("Aún no se han generado números. Por favor, genere los números primero")
                else:
                    mostrarNumeros(arreglo)
            case 'b':
                if not arreglo:
                    print("Aún no se han generado números. Por favor, genere los números primero")
                else:
                    mostrarPromedio(arreglo)
            case 'c':
                if not arreglo:
                    print("Aún no se han generado números. Por favor, genere los números primero")
                else:
                    mostrarLongitud(arreglo)
            case 'd':
                if not arreglo:
                    print("Aún no se han generado números. Por favor, genere los números primero")
                else:
                    sumarPosicionesPares(arreglo)
                    sumarPosicionesImpares(arreglo)
            case 'q':
                print("Ha salido del programa.")
                return
            case _:
                print("Opción no válida. Seleccione una opción válida")

if __name__ == "__main__":
    main()


print("\nSemana No. 12: Ejercicio 2")

def solicitarDimensiones():
    while True:
        try:
            filas = int(input("Ingrese la cantidad de filas de la matriz: "))
            columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
            if filas > 0 and columnas > 0:
                return filas, columnas
            else:
                print("Por favor, ingrese valores válidos (mayores que 0)")
        except ValueError:
            print("Por favor, ingrese valores válidos (números enteros)")

def poblarMatriz(filas, columnas):
    matriz = [[random.randint(0, 1000) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def mostrarMatriz(matriz):
    print("Matriz generada:")
    for fila in matriz:
        print(fila)

def calcularEstadisticas(matriz):
    numerosPares = sum(1 for fila in matriz for elemento in fila if elemento % 2 == 0)
    numerosImpares = sum(1 for fila in matriz for elemento in fila if elemento % 2 != 0)
    numeroMayor = max(max(fila) for fila in matriz)
    numeroMenor = min(min(fila) for fila in matriz)
    print("Estadísticas:")
    print("a. Cantidad de números pares:", numerosPares)
    print("b. Cantidad de números impares:", numerosImpares)
    print("c. Número mayor:", numeroMayor)
    print("d. Número menor:", numeroMenor)

def main():
    filas, columnas = solicitarDimensiones()
    matriz = poblarMatriz(filas, columnas)
    mostrarMatriz(matriz)
    calcularEstadisticas(matriz)

if __name__ == "__main__":
    main()
