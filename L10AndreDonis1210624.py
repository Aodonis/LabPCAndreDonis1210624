#Actividad No. 01
print("Semana No. 10: Ejercicio 1")

numeromes = int(input("Ingrese el número de mes: "))

if numeromes < 1 or numeromes > 12:
    print("¡Error!: El número a ingresar debe estar contenido entre 1 y 12")
else:
    if numeromes == 1:
        nombremes = "Enero"
    elif numeromes == 2:
        nombremes = "Febrero"
    elif numeromes == 3:
        nombremes = "Marzo"
    elif numeromes == 4:
        nombremes = "Abril"
    elif numeromes == 5:
        nombremes = "Mayo"
    elif numeromes == 6:
        nombremes = "Junio"
    elif numeromes == 7:
        nombremes = "Julio"
    elif numeromes == 8:
        nombremes = "Agosto"
    elif numeromes == 9:
        nombremes = "Septiembre"
    elif numeromes == 10:
        nombremes = "Octubre"
    elif numeromes == 11:
        nombremes = "Noviembre"
    else:
        nombremes = "Diciembre"
    
    print(f"MES:", nombremes)

#Actividad No. 02
print("Semana No 10: Ejercicio 2")

a = int(input("Ingrese un primer número: "))
b = int(input("Ingrese un segundo número: "))
c = int(input("Ingrese un tercer número: "))

if (a <= 0 or b <= 0 or c <= 0):
    print("¡Error!: Ingresa un número mayor a 0")

if a > b: 
    if a > c: 
        print("A es el mayor")
    else: 
        if a == c: 
            print("A es mayor a B, A es igual a C")
        else:
            print("A es mayor a B, A es menor a C")
elif a == b: 
    if a > c:
        print("A es igual a B, A mayor que C")
elif a == c:
    print("A es igual a B y C")
else: 
    print("A es igual a B y menor que C")
if b > c: 
    print("B igual a A y mayor que C")
elif b == c: 
    print("B es igual a A e igual a C")
else: 
    print("B es igual a A y menor que C")