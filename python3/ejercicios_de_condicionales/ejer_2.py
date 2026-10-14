clave_guardada = "contraseña"
clave_usuario = input("Introduce la contraseña: ")

if clave_guardada.lower() == clave_usuario.lower():
    print("La contraseña coincide.")
else:
    print("La contraseña no coincide.")