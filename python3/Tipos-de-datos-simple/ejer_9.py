inversion = float(input("Inversión: "))
interes = float(input("Interés anual (%): "))
anios = int(input("Años: "))

print("Capital obtenido:", inversion * (1 + interes / 100) ** anios)