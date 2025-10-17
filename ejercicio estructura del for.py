# Cálculo del total a pagar en un restaurante

print(" BIENVENIDO AL RESTAURANTE SABOR CUCUTEÑO")
print("----------------------------------------------")

# Pedimos cuántos platos va a registrar el usuario
cantidad = int(input("Cuántos platos desea registrar: "))

# Creamos una lista vacía para guardar los precios
precios = []

# Ciclo para ingresar el precio de cada plato
for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del plato {i + 1}: $"))
    precios.append(precio)

# Calculamos el total de la cuenta
total = sum(precios)

# Mostramos los resultados
print("\n Detalle de la cuenta:")
for i, valor in enumerate(precios, start=1):
    print(f"Plato {i}: ${valor:.2f}")

print("----------------------------------------------")
print(f" Total a pagar: ${total:.2f}")
print("Gracias por su visita, vuelva pronto")
