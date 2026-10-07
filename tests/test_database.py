import database


def test_crud_database(tmp_path, monkeypatch):
    base_datos_prueba = tmp_path / "test_helpdesk.db"

    monkeypatch.setattr(
        database,
        "DATABASE",
        str(base_datos_prueba)
    )

    database.crear_tabla()

    database.insertar_incidencia(
        "Rafa",
        "No funciona internet"
    )

    incidencias = database.obtener_incidencias()

    assert len(incidencias) == 1
    assert incidencias[0][0] == 1
    assert incidencias[0][1] == "Rafa"
    assert incidencias[0][2] == "No funciona internet"
    assert incidencias[0][3] == 0

    cerrada = database.cerrar_incidencia_db(1)

    assert cerrada is True

    incidencias = database.obtener_incidencias()

    assert incidencias[0][3] == 1

    eliminada = database.eliminar_incidencia_db(1)

    assert eliminada is True

    incidencias = database.obtener_incidencias()

    assert incidencias == []