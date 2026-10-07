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
        json.dump(
            incidencias,
            archivo,
            indent=4,
            ensure_ascii=False
        )