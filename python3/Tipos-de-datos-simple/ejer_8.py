# Pedir dos números enteros al usuario
n = int(input("Introduce el dividendo (n): "))
m = int(input("Introduce el divisor (m): "))

# Verificar que el divisor no sea cero para evitar un error de división
if m != 0:
    # Calcular el cociente y el resto de la división entera
    c = n // m
    r = n % m

    # Mostrar el resultado utilizando separadores por coma (sin usar llaves)
    print(n, "entre", m, "da un cociente", c, "y un resto", r)
else:
    print("Error: No se puede dividir entre cero.")

    