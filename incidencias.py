from almacenamiento import guardar_incidencias


def crear_incidencia(incidencias):
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


def ver_incidencias(incidencias):
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


def cerrar_incidencia(incidencias):
    try:
        id_buscado = int(
            input("ID de la incidencia que quieres cerrar: ")
        )

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