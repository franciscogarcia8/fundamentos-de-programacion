n = int(input("Introduce un número entero positivo: "))

if n > 0:
    suma = n * (n + 1) // 2
    
    # Imprime usando comas para separar el texto de las variables
    print("La suma de los enteros desde 1 hasta", n, "es:", suma)
else:
    print("El número introducido debe ser mayor que 0.")