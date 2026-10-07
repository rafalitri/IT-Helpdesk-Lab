from incidencias import ver_incidencias, cerrar_incidencia


def test_ver_incidencias_pendiente(capsys):
    incidencias = [
        {
            "id": 1,
            "usuario": "Rafa",
            "problema": "No funciona internet",
            "resuelta": False
        }
    ]

    ver_incidencias(incidencias)

    salida = capsys.readouterr().out

    assert "1 - Rafa - No funciona internet - PENDIENTE" in salida


def test_ver_incidencias_resuelta(capsys):
    incidencias = [
        {
            "id": 2,
            "usuario": "Bea",
            "problema": "No enciende el PC",
            "resuelta": True
        }
    ]

    ver_incidencias(incidencias)

    salida = capsys.readouterr().out

    assert "2 - Bea - No enciende el PC - RESUELTA" in salida


def test_ver_incidencias_vacia(capsys):
    incidencias = []

    ver_incidencias(incidencias)

    salida = capsys.readouterr().out

    assert "No hay incidencias" in salida

def test_cerrar_incidencia(capsys, monkeypatch):
    incidencias = [
        {
            "id": 1,
            "usuario": "Rafa",
            "problema": "No funciona internet",
            "resuelta": False
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr("incidencias.guardar_incidencias", lambda _: None)

    cerrar_incidencia(incidencias)

    salida = capsys.readouterr().out

    assert incidencias[0]["resuelta"] is True
    assert "Incidencia cerrada correctamente" in salida