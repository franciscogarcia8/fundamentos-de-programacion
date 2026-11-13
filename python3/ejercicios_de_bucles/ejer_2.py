 # Pedir al usuario su edad y convertirla a entero
edad = int(input("¿Cuántos años tienes? "))

# Recorrer desde 1 hasta la edad ingresada (inclusive)
for i in range(1, edad + 1):
	print("Has cumplido", i, "años")
