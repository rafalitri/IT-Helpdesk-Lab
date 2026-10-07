import logging

from database import crear_tabla
from incidencias import crear_incidencia, ver_incidencias, cerrar_incidencia
from diagnostico import mostrar_info_sistema, mostrar_info_red


logging.basicConfig(
    filename="helpdesk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

crear_tabla()


while True:
    print("1. Crear incidencia")
    print("2. Ver incidencias")
    print("3. Cerrar incidencia")
    print("4. Diagnóstico del sistema")
    print("5. Diagnóstico de red")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_incidencia()

    elif opcion == "2":
        ver_incidencias()

    elif opcion == "3":
        cerrar_incidencia()

    elif opcion == "4":
        mostrar_info_sistema()

    elif opcion == "5":
        mostrar_info_red()

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción incorrecta")