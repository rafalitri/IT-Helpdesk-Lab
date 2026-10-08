import logging

from database import (
    insertar_incidencia,
    obtener_incidencias,
    cerrar_incidencia_db,
    obtener_todas_incidencias_con_tecnico,
    insertar_tecnico,
    obtener_tecnicos,
    obtener_incidencias_pendientes,
    asignar_tecnico
)


def crear_incidencia():
    usuario = input("Nombre del usuario: ").strip()
    problema = input("Describe el problema: ").strip()

    if not usuario or not problema:
        print("El usuario y el problema no pueden estar vacíos.")
        logging.warning("Intento de crear una incidencia con datos vacíos")
        return

    insertar_incidencia(usuario, problema)

    logging.info(
        "Nueva incidencia creada para el usuario %s",
        usuario
    )

    print("Incidencia guardada correctamente")


def ver_incidencias():
    incidencias = obtener_incidencias()

    if not incidencias:
        print("No hay incidencias")
        return

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


def ver_incidencias_con_tecnico():
    incidencias = obtener_todas_incidencias_con_tecnico()

    if not incidencias:
        print("No hay incidencias")
        return

    for incidencia in incidencias:
        id_incidencia = incidencia[0]
        usuario = incidencia[1]
        problema = incidencia[2]
        tecnico = incidencia[3]

        if tecnico is None:
            tecnico = "SIN ASIGNAR"

        print(
            id_incidencia,
            "-",
            usuario,
            "-",
            problema,
            "- Técnico:",
            tecnico
        )


def crear_tecnico():
    nombre = input("Nombre del técnico: ").strip()

    if not nombre:
        print("El nombre del técnico no puede estar vacío.")
        return

    insertar_tecnico(nombre)

    print("Técnico creado correctamente")


def ver_tecnicos():
    tecnicos = obtener_tecnicos()

    if not tecnicos:
        print("No hay técnicos")
        return

    print("\n=== TÉCNICOS ===")

    for tecnico in tecnicos:
        print(
            tecnico[0],
            "-",
            tecnico[1]
        )


def asignar_tecnico_a_incidencia():
    incidencias = obtener_incidencias_pendientes()
    tecnicos = obtener_tecnicos()

    if not incidencias:
        print("No hay incidencias pendientes.")
        return

    if not tecnicos:
        print("No hay técnicos disponibles.")
        return

    print("\n=== INCIDENCIAS PENDIENTES ===")

    for incidencia in incidencias:
        print(
            incidencia[0],
            "-",
            incidencia[1],
            "-",
            incidencia[2]
        )

    print("\n=== TÉCNICOS ===")

    for tecnico in tecnicos:
        print(
            tecnico[0],
            "-",
            tecnico[1]
        )

    try:
        id_incidencia = int(
            input("ID de la incidencia: ")
        )

        id_tecnico = int(
            input("ID del técnico: ")
        )

    except ValueError:
        print("Los IDs tienen que ser números.")
        return

    incidencia_existe = any(
        incidencia[0] == id_incidencia
        for incidencia in incidencias
    )

    tecnico_existe = any(
        tecnico[0] == id_tecnico
        for tecnico in tecnicos
    )

    if not incidencia_existe:
        print("La incidencia no existe o no está pendiente.")
        return

    if not tecnico_existe:
        print("El técnico no existe.")
        return

    asignar_tecnico(
        id_incidencia,
        id_tecnico
    )

    print("Técnico asignado correctamente")