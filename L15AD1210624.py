#AndreDonis1210624

import math

print("Semana No. 12: Ejercicio 1")
print("Actividad 1")


def mostrarmenu():
    print("Opciones:")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")

def calcularareatriangulo(base, altura):
    return 0.5 * base * altura

def calcularareacuadrado(lado):
    return lado * lado

def calculararearectangulo(base, altura):
    return base * altura

def calcularareacirculo(radio):
    return math.pi * radio ** 2

def main():
    mostrarmenu()
    opcion = input("Ingrese la opción que desea calcular: ").lower()

    match opcion:
        case 'a':
            base = float(input("Ingrese la longitud de la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcularareatriangulo(base, altura)
            print("El área del triángulo es:", area)
        case 'b':
            lado = float(input("Ingrese la longitud del lado del cuadrado: "))
            area = calcularareacuadrado(lado)
            print("El área del cuadrado es:", area)
        case 'c':
            base = float(input("Ingrese la longitud de la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calculararearectangulo(base, altura)
            print("El área del rectángulo es:", area)
        case 'd':
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcularareacirculo(radio)
            print("El área del círculo es:", area)
        case _:
            print("Opción no válida")

if __name__ == "__main__":
    main()


print("\nActividad 2")

X = 0
Y = 0

def moverarriba():
    global Y
    Y += 1

def moverabajo():
    global Y
    Y -= 1

def moverderecha():
    global X
    X += 1

def moverizquierda():
    global X
    X -= 1

def main():
    while True:
        print("\nCoordenadas actuales del personaje: ({}, {})".format(X, Y))
        print("Opciones:")
        print("a. Sube")
        print("b. Baja")
        print("c. Izquierda")
        print("d. Derecha")
        print("e. Salir")

        opcion = input("Seleccione una opción: ").lower()

        match opcion:
            case 'a':
                moverarriba()
            case 'b':
                moverabajo()
            case 'c':
                moverizquierda()
            case 'd':
                moverderecha()
            case 'e':
                print("Coordenadas finales del personaje: {}, {}".format(X, Y))
                return
            case _:
                print("Opción no válida. Por favor, seleccionar una opción válida.")

if __name__ == "__main__":
    main()