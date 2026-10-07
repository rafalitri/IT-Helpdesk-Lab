import requests

import api_client


def test_api_timeout(capsys, monkeypatch):
    def simular_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout

    monkeypatch.setattr(
        requests,
        "request",
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
        "request",
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
        "request",
        lambda *args, **kwargs: RespuestaFalsa()
    )

    api_client.obtener_datos_api()

    salida = capsys.readouterr().out

    assert "error HTTP" in salida


def test_hacer_peticion_correcta(monkeypatch):
    class RespuestaFalsa:
        status_code = 200

        def raise_for_status(self):
            pass

    def request_falso(metodo, url, timeout, **kwargs):
        assert metodo == "POST"
        assert url == "https://ejemplo.com/api"
        assert timeout == 5
        assert kwargs == {
            "json": {"nombre": "Rafa"}
        }

        return RespuestaFalsa()

    monkeypatch.setattr(
        requests,
        "request",
        request_falso
    )

    respuesta = api_client.hacer_peticion(
        "POST",
        "https://ejemplo.com/api",
        json={"nombre": "Rafa"}
    )

    assert respuesta.status_code == 200


def test_hacer_peticion_devuelve_none_si_falla(monkeypatch):
    def request_falso(*args, **kwargs):
        raise requests.exceptions.Timeout

    monkeypatch.setattr(
        requests,
        "request",
        request_falso
    )

    respuesta = api_client.hacer_peticion(
        "GET",
        "https://ejemplo.com/api"
    )

    assert respuesta is None