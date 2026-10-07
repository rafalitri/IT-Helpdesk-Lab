import logging

from database import (
    insertar_incidencia,
    obtener_incidencias,
    cerrar_incidencia_db
)

def crear_incidencia():
    usuario = input("Nombre del usuario: ")
    problema = input("Describe el problema: ")

    insertar_incidencia(usuario, problema)

    logging.info(
        "Nueva incidencia creada para el usuario %s",
        usuario
    )

    print("Incidencia guardada correctamente")


def ver_incidencias():
    incidencias = obtener_incidencias()

    if len(incidencias) == 0:
        print("No hay incidencias")
    else:
        for incidencia in incidencias:
            if incidencia[3]:
                estado = "RESUELTA"
            else:
                estado = "PENDIENTE"

            print(
                incidencia[0],
                "-",
                incidencia[1],
                "-",
                incidencia[2],
                "-",
                estado
            )


def cerrar_incidencia():
    try:
        id_buscado = int(
            input("ID de la incidencia que quieres cerrar: ")
        )

        incidencias = obtener_incidencias()

        encontrada = False

        for incidencia in incidencias:
            if incidencia[0] == id_buscado:
                encontrada = True
                break

        if encontrada:
            cerrar_incidencia_db(id_buscado)

            logging.info(
                "Incidencia %s cerrada",
                id_buscado
            )

            print("Incidencia cerrada correctamente")

        else:
            logging.warning(
                "Se intentó cerrar un ID inexistente: %s",
                id_buscado
            )

            print("No existe una incidencia con ese ID")

    except ValueError:
        logging.warning("Se introdujo un ID no numérico")
        print("El ID tiene que ser un número")