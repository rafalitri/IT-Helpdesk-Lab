from almacenamiento import cargar_incidencias
from incidencias import crear_incidencia, ver_incidencias, cerrar_incidencia


incidencias = cargar_incidencias()

while True:
    print("\n=== IT HELPDESK LAB ===")
    print("1. Crear incidencia")
    print("2. Ver incidencias")
    print("3. Cerrar incidencia")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_incidencia(incidencias)

    elif opcion == "2":
        ver_incidencias(incidencias)

    elif opcion == "3":
        cerrar_incidencia(incidencias)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción incorrecta")