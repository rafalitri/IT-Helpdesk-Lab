import requests

import api_client


def test_api_timeout(capsys, monkeypatch):
    def simular_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout

    monkeypatch.setattr(
        requests,
        "get",
        simular_timeout
    )

    api_client.obtener_datos_api()

    salida = capsys.readouterr().out

    assert "ha tardado demasiado" in salida


def test_api_error_conexion(capsys, monkeypatch):
    def simular_error_conexion(*args, **kwargs):
        raise requests.exceptions.ConnectionError

    monkeypatch.setattr(
        requests,
        "get",
        simular_error_conexion
    )

    api_client.obtener_datos_api()

    salida = capsys.readouterr().out

    assert "No se pudo conectar con la API" in salida


def test_api_error_http(capsys, monkeypatch):
    class RespuestaFalsa:
        status_code = 404

        def raise_for_status(self):
            raise requests.exceptions.HTTPError(
                "404 Client Error"
            )

    monkeypatch.setattr(
        requests,
        "get",
        lambda *args, **kwargs: RespuestaFalsa()
    )

    api_client.obtener_datos_api()

    salida = capsys.readouterr().out

    assert "error HTTP" in salida