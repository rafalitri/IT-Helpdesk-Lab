from incidencias import (
    crear_incidencia,
    ver_incidencias,
    cerrar_incidencia,
    ver_incidencias_con_tecnico,
    crear_tecnico,
    ver_tecnicos,
    asignar_tecnico_a_incidencia
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


def test_ver_incidencias_con_tecnico(capsys, monkeypatch):
    datos = [
        (1, "Rafa", "No funciona internet", "Carlos"),
        (2, "Bea", "No funciona Outlook", None)
    ]

    monkeypatch.setattr(
        "incidencias.obtener_todas_incidencias_con_tecnico",
        lambda: datos
    )

    ver_incidencias_con_tecnico()

    salida = capsys.readouterr().out

    assert "Rafa - No funciona internet - Técnico: Carlos" in salida
    assert "Bea - No funciona Outlook - Técnico: SIN ASIGNAR" in salida


def test_crear_tecnico(capsys, monkeypatch):
    llamadas = []

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Carlos"
    )

    monkeypatch.setattr(
        "incidencias.insertar_tecnico",
        lambda nombre: llamadas.append(nombre)
    )

    crear_tecnico()

    salida = capsys.readouterr().out

    assert llamadas == ["Carlos"]
    assert "Técnico creado correctamente" in salida


def test_ver_tecnicos(capsys, monkeypatch):
    tecnicos = [
        (1, "Carlos"),
        (2, "Ana")
    ]

    monkeypatch.setattr(
        "incidencias.obtener_tecnicos",
        lambda: tecnicos
    )

    ver_tecnicos()

    salida = capsys.readouterr().out

    assert "1 - Carlos" in salida
    assert "2 - Ana" in salida


def test_asignar_tecnico_a_incidencia(capsys, monkeypatch):
    incidencias_pendientes = [
        (3, "Carlos", "No funciona el teclado", 0)
    ]

    tecnicos = [
        (1, "Carlos")
    ]

    llamadas = []

    entradas = iter([
        "3",
        "1"
    ])

    monkeypatch.setattr(
        "incidencias.obtener_incidencias_pendientes",
        lambda: incidencias_pendientes
    )

    monkeypatch.setattr(
        "incidencias.obtener_tecnicos",
        lambda: tecnicos
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    monkeypatch.setattr(
        "incidencias.asignar_tecnico",
        lambda incidencia_id, tecnico_id:
        llamadas.append((incidencia_id, tecnico_id))
    )

    asignar_tecnico_a_incidencia()

    salida = capsys.readouterr().out

    assert llamadas == [(3, 1)]
    assert "Técnico asignado correctamente" in salida