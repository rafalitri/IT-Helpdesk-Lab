import json
import os

ARCHIVO = "incidencias.json"


def cargar_incidencias():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_incidencias(incidencias):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(incidencias, archivo, indent=4, ensure_ascii=False)


incidencias = cargar_incidencias()

print("=== IT HELPDESK LAB ===")
print("1. Crear incidencia")
print("2. Ver incidencias")
print("3. Cerrar incidencia")
print("4. Salir")

opcion = input("Selecciona una opción: ")

if opcion == "1":
    usuario = input("Nombre del usuario: ")
    problema = input("Describe el problema: ")

    nuevo_id = len(incidencias) + 1

    incidencia = {
        "id": nuevo_id,
        "usuario": usuario,
        "problema": problema,
        "resuelta": False
    }

    incidencias.append(incidencia)
    guardar_incidencias(incidencias)

    print("Incidencia guardada correctamente")

elif opcion == "2":
    if len(incidencias) == 0:
        print("No hay incidencias")
    else:
        for incidencia in incidencias:
            if incidencia["resuelta"]:
                estado = "RESUELTA"
            else:
                estado = "PENDIENTE"

            print(
                incidencia["id"],
                "-",
                incidencia["usuario"],
                "-",
                incidencia["problema"],
                "-",
                estado
            )

elif opcion == "3":
    try:
        id_buscado = int(input("ID de la incidencia que quieres cerrar: "))

        encontrada = False

        for incidencia in incidencias:
            if incidencia["id"] == id_buscado:
                incidencia["resuelta"] = True
                encontrada = True
                break

        if encontrada:
            guardar_incidencias(incidencias)
            print("Incidencia cerrada correctamente")
        else:
            print("No existe una incidencia con ese ID")

    except ValueError:
        print("El ID tiene que ser un número")

elif opcion == "4":
    print("Saliendo del programa...")

else:
    print("Opción incorrecta")