import database


def test_crud_database(tmp_path, monkeypatch):
    base_datos_prueba = tmp_path / "test_helpdesk.db"

    monkeypatch.setattr(
        database,
        "DATABASE",
        str(base_datos_prueba)
    )

    database.crear_tabla()

    # Crear incidencias
    database.insertar_incidencia(
        "Rafa",
        "No funciona internet"
    )

    database.insertar_incidencia(
        "Bea",
        "No funciona Outlook"
    )

    # Crear técnico y asignarlo a la incidencia 1
    database.insertar_tecnico("Carlos")
    database.asignar_tecnico(1, 1)

    # Comprobar INNER JOIN:
    # solo aparecen incidencias con técnico asignado
    asignadas = database.obtener_incidencias_con_tecnico()

    assert len(asignadas) == 1
    assert asignadas[0][0] == 1
    assert asignadas[0][1] == "Rafa"
    assert asignadas[0][2] == "No funciona internet"
    assert asignadas[0][3] == "Carlos"

    # Comprobar LEFT JOIN:
    # aparecen todas las incidencias, tengan técnico o no
    todas_asignaciones = database.obtener_todas_incidencias_con_tecnico()

    assert len(todas_asignaciones) == 2

    assert todas_asignaciones[0][0] == 1
    assert todas_asignaciones[0][1] == "Rafa"
    assert todas_asignaciones[0][2] == "No funciona internet"
    assert todas_asignaciones[0][3] == "Carlos"

    assert todas_asignaciones[1][0] == 2
    assert todas_asignaciones[1][1] == "Bea"
    assert todas_asignaciones[1][2] == "No funciona Outlook"
    assert todas_asignaciones[1][3] is None

    # Comprobar incidencias
    incidencias = database.obtener_incidencias()

    assert len(incidencias) == 2

    assert incidencias[0][0] == 1
    assert incidencias[0][1] == "Rafa"
    assert incidencias[0][2] == "No funciona internet"
    assert incidencias[0][3] == 0

    assert incidencias[1][0] == 2
    assert incidencias[1][1] == "Bea"
    assert incidencias[1][2] == "No funciona Outlook"
    assert incidencias[1][3] == 0

    # Cerrar incidencia 1
    cerrada = database.cerrar_incidencia_db(1)

    assert cerrada is True

    # Obtener solo las incidencias pendientes
    pendientes = database.obtener_incidencias_pendientes()

    assert len(pendientes) == 1
    assert pendientes[0][1] == "Bea"
    assert pendientes[0][2] == "No funciona Outlook"
    assert pendientes[0][3] == 0

    # Contar incidencias pendientes
    cantidad_pendientes = database.contar_incidencias_pendientes()

    assert cantidad_pendientes == 1

    # Agrupar y contar incidencias por estado
    resumen = database.contar_incidencias_por_estado()

    assert resumen == [
        (0, 1),
        (1, 1)
    ]

    # Eliminar incidencia 1
    eliminada = database.eliminar_incidencia_db(1)

    assert eliminada is True

    # Comprobar que solamente queda Bea
    incidencias = database.obtener_incidencias()

    assert len(incidencias) == 1
    assert incidencias[0][1] == "Bea"