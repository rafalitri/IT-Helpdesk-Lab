print("=== IT HELPDESK LAB ===")
print("1. Crear incidencia")
print("2. Ver incidencias")
print("3. Salir")

opcion = input("Selecciona una opción: ")

print("Has seleccionado la opción", opcion)

if opcion == "1":
    usuario = input("Nombre del usuario: ")
    problema = input("Describe el problema: ")

    incidencia = {
        "usuario": usuario,
        "problema": problema,
        "resuelta": False
    }

    print("Incidencia creada:")
    print(incidencia)

elif opcion == "2":
    print("Ver incidencias")

elif opcion == "3":
    print("Saliendo del programa...")

else:
    print("Opción incorrecta")