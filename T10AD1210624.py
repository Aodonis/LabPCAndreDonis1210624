print("Nombre: André Donis")
print("Carné: 1210624")

dia = int(input("Ingrese el día de su fecha de nacimiento (1-31): "))
mes = int(input("Ingrese el mes de su fecha de nacimiento (1-12): "))
año = int(input("Ingrese el año de su fecha de nacimiento (XXXX): "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo_zodiacal = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo_zodiacal = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo_zodiacal = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo_zodiacal = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo_zodiacal = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo_zodiacal = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo_zodiacal = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo_zodiacal = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo_zodiacal = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo_zodiacal = "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo_zodiacal = "Acuario"
else:
    signo_zodiacal = "Piscis"

print("Su signo zodiacal es:", signo_zodiacal)
