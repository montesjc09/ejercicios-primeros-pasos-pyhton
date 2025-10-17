# programa para identificar si el numero es pa o impar

numero = 0 # la variable empieza con cero

# se solicita un valor
numero = int(input(" digite un numero: "))

# se mira si el numero es par o impar
if numero % 2 == 0:
    print("el numero", numero, "es Par" )
else:
    print("el numero", numero, "es Impar")