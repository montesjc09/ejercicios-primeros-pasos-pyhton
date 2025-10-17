# programa para identificar si un numero es positivo negativo o neutro

# solicitar al usuario que ingrese un numero
numero = float(input("ingrese un numero: "))

# estructura if elif else
if numero > 0:
    print("el numero es positivo.")
elif numero < 0:
    print("el numero es negativo.")
else:
    print("el numero es neutro (cero).")    