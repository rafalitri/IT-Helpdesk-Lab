from incidencias import ver_incidencias, cerrar_incidencia


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
    incidencias = [
        (1, "Rafa", "No funciona internet", 0)
    ]

    llamadas = []

    monkeypatch.setattr("builtins.input", lambda _: "1")

    monkeypatch.setattr(
        "incidencias.obtener_incidencias",
        lambda: incidencias
    )

    monkeypatch.setattr(
        "incidencias.cerrar_incidencia_db",
        lambda id_incidencia: llamadas.append(id_incidencia)
    )

    cerrar_incidencia()

    salida = capsys.readouterr().out

    assert llamadas == [1]
    assert "Incidencia cerrada correctamente" in salida


def test_cerrar_incidencia_id_inexistente(capsys, monkeypatch):
    incidencias = [
        (1, "Rafa", "No funciona internet", 0)
    ]

    llamadas = []

    monkeypatch.setattr("builtins.input", lambda _: "99")

    monkeypatch.setattr(
        "incidencias.obtener_incidencias",
        lambda: incidencias
    )

    monkeypatch.setattr(
        "incidencias.cerrar_incidencia_db",
        lambda id_incidencia: llamadas.append(id_incidencia)
    )

    cerrar_incidencia()

    salida = capsys.readouterr().out

    assert llamadas == []
    assert "No existe una incidencia con ese ID" in salida


def test_cerrar_incidencia_id_no_numerico(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "abc")

    cerrar_incidencia()

    salida = capsys.readouterr().out

    assert "El ID tiene que ser un número" in salida