# Preguntamos al usuario el tipo de pizza que desea
tipo = input("¿Quieres una pizza vegetariana? (si/no): ").lower()
if tipo == "si":
    print("\nIngredientes vegetarianos disponibles:")
    print("1 - Pimiento")
    print("2 - Tofu")
    
    opcion = input("Elige un ingrediente (1 o 2): ")
    
    if opcion == "1":
        ingrediente = "Pimiento"
    else:
        ingrediente = "Tofu"
        
    print("\nHas elegido una pizza vegetariana.")
    print(f"Ingredientes: Tomate, Mozzarella y {ingrediente}.")

else:
    print("\nIngredientes no vegetarianos disponibles:")
    print("1 - Peperoni")
    print("2 - Jamón")
    print("3 - Salmón")
    
    opcion = input("Elige un ingrediente (1, 2 o 3): ")
    
    if opcion == "1":
        ingrediente = "Peperoni"
    elif opcion == "2":
        ingrediente = "Jamón"
    else:
        ingrediente = "Salmón"
        
    print("\nHas elegido una pizza no vegetariana.")
    print(f"Ingredientes: Tomate, Mozzarella y {ingrediente}.")