puntuacion = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None
if nivel is not None:
    dinero = puntuacion * 2400
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Cantidad de dinero a recibir: {dinero:.2f}€")
else:
    print("Puntuación no válida. Solo se permite 0.0, 0.4 o 0.6 en adelante.")