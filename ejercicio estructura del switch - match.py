# mostrar el mes según el número

print("===== CALENDARIO DEL AÑO =====")
print("1. Enero")
print("2. Febrero")
print("3. Marzo")
print("4. Abril")
print("5. Mayo")
print("6. Junio")
print("7. Julio")
print("8. Agosto")
print("9. Septiembre")
print("10. Octubre")
print("11. Noviembre")
print("12. Diciembre")
print("==============================")

# Solicitar número del mes al usuario
numero_mes = int(input("Digite el número del mes que desea consultar: "))

# Lista con los nombres de los meses
meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Mostrar el resultado
if 1 <= numero_mes <= 12:
    print(f"El mes número {numero_mes} es {meses[numero_mes - 1]}.")
else:
    print(" Número inválido debe estar entre 1 y 12.")
