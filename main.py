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
print("3. Salir")

opcion = input("Selecciona una opción: ")

if opcion == "1":
    usuario = input("Nombre del usuario: ")
    problema = input("Describe el problema: ")

    incidencia = {
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
            print(
                incidencia["usuario"],
                "-",
                incidencia["problema"]
            )

elif opcion == "3":
    print("Saliendo del programa...")

else:
    print("Opción incorrecta")