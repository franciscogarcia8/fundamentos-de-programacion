producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

coste_total = precio * unidades

print(f"{producto}: {precio:09.2f} € | {unidades:03d} unidades | Total: {coste_total:011.2f} €")