from incidencias import (
    crear_incidencia,
    ver_incidencias,
    cerrar_incidencia
)


def test_crear_incidencia(capsys, monkeypatch):
    entradas = iter([
        "Rafa",
        "No funciona internet"
    ])

    llamadas = []

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    monkeypatch.setattr(
        "incidencias.insertar_incidencia",
        lambda usuario, problema: llamadas.append(
            (usuario, problema)
        )
    )

    crear_incidencia()

    salida = capsys.readouterr().out

    assert llamadas == [
        ("Rafa", "No funciona internet")
    ]
    assert "Incidencia guardada correctamente" in salida


def test_crear_incidencia_vacia(capsys, monkeypatch):
    entradas = iter([
        "",
        ""
    ])

    llamadas = []

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    monkeypatch.setattr(
        "incidencias.insertar_incidencia",
        lambda usuario, problema: llamadas.append(
            (usuario, problema)
        )
    )

    crear_incidencia()

    salida = capsys.readouterr().out

    assert llamadas == []
    assert "no pueden estar vacíos" in salida


def test_ver_incidencias_pendiente(capsys, monkeypatch):
    incidencias = [
        (1, "Rafa", "No funciona internet", 0)
    ]

    monkeypatch.setattr(
        "incidencias.obtener_incidencias",
        lambda: incidencias
    )

    ver_incidencias()

    salida = capsys.readouterr().out

    assert "1 - Rafa - No funciona internet - PENDIENTE" in salida


def test_ver_incidencias_resuelta(capsys, monkeypatch):
    incidencias = [
        (2, "Bea", "No enciende el PC", 1)
    ]

    monkeypatch.setattr(
        "incidencias.obtener_incidencias",
        lambda: incidencias
    )

    ver_incidencias()

    salida = capsys.readouterr().out

    assert "2 - Bea - No enciende el PC - RESUELTA" in salida


def test_ver_incidencias_vacia(capsys, monkeypatch):
    monkeypatch.setattr(
        "incidencias.obtener_incidencias",
        lambda: []
    )

    ver_incidencias()

    salida = capsys.readouterr().out

    assert "No hay incidencias" in salida


def test_cerrar_incidencia(capsys, monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    monkeypatch.setattr(
        "incidencias.cerrar_incidencia_db",
        lambda id_incidencia: True
    )

    cerrar_incidencia()

    salida = capsys.readouterr().out

    assert "Incidencia cerrada correctamente" in salida


def test_cerrar_incidencia_id_inexistente(capsys, monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    monkeypatch.setattr(
        "incidencias.cerrar_incidencia_db",
        lambda id_incidencia: False
    )

    cerrar_incidencia()

    salida = capsys.readouterr().out

    assert "No existe una incidencia con ese ID" in salida


def test_cerrar_incidencia_id_no_numerico(capsys, monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "abc"
    )

    cerrar_incidencia()

    salida = capsys.readouterr().out

    assert "El ID tiene que ser un número" in salida