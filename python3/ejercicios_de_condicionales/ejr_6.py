nombre = input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo (M para mujer, H para hombre)? ").upper()

primera_letra = nombre[0].upper()
if (sexo == "M" and primera_letra < "M") or (sexo == "H" and primera_letra > "N"):
    grupo = "A"
else:
    grupo = "B"
print(f"Te corresponde el grupo {grupo}.")