# Programa con menú de opciones en Python

def mostrar_menu():
    print("///////////////////////////////////////")
    print("         Menu")
    print("///////////////////////////////////////")
    print("1. Saludar al usuario")
    print("2. Calcular si un número es positivo, negativo o neutro")
    print("3. Mostrar una lista de números")
    print("4. Salir del programa")
    print("///////////////////////////////////////")

# Función para identificar tipo de número
def tipo_numero():
    try:
        numero = float(input("Ingrese un número: "))
        if numero > 0:
            print("El número es positivo.")
        elif numero < 0:
            print("El número es negativo.")
        else:
            print("El número es neutro (cero).")
    except ValueError:
        print("Error: debe ingresar un número válido.")

# Función para mostrar una lista
def mostrar_lista():
    lista = [10, 20, 30, 40, 50]
    print("Lista de números:", lista)

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        print(f"¡Hola, {nombre}! ")
    elif opcion == "2":
        tipo_numero()
        print()
    elif opcion == "3":
        mostrar_lista()
        print()
    elif opcion == "4":
        print("Gracias por usar el programa. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Intente nuevamente.\n")
