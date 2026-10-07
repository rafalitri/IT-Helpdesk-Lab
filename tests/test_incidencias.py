from incidencias import ver_incidencias


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