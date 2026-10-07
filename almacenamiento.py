import logging
import json
import os

ARCHIVO = "incidencias.json"


def cargar_incidencias():
    if not os.path.exists(ARCHIVO):
        logging.info("No existe el archivo de incidencias. Se inicia una lista vacía.")
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except json.JSONDecodeError:
        logging.error("El archivo de incidencias contiene JSON no válido.")
        return []


def guardar_incidencias(incidencias):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(
            incidencias,
            archivo,
            indent=4,
            ensure_ascii=False
        )