import almacenamiento


def test_cargar_incidencias_json_invalido(tmp_path, monkeypatch):
    archivo_prueba = tmp_path / "incidencias.json"

    archivo_prueba.write_text(
        "esto no es json valido",
        encoding="utf-8"
    )

    monkeypatch.setattr(
        almacenamiento,
        "ARCHIVO",
        str(archivo_prueba)
    )

    incidencias = almacenamiento.cargar_incidencias()

    assert incidencias == []
    