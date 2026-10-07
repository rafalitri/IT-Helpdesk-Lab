import socket

import diagnostico


def test_diagnostico_red_correcto(capsys, monkeypatch):
    monkeypatch.setattr(
        socket,
        "gethostname",
        lambda: "PC-PRUEBA"
    )

    def resolver_dns(host):
        if host == "PC-PRUEBA":
            return "192.168.1.100"

        return "93.184.216.34"

    monkeypatch.setattr(
        socket,
        "gethostbyname",
        resolver_dns
    )

    monkeypatch.setattr(
        diagnostico,
        "comprobar_ping",
        lambda: True
    )

    diagnostico.mostrar_info_red()

    salida = capsys.readouterr().out

    assert "IP local: 192.168.1.100" in salida
    assert "DNS funcionando" in salida
    assert "La conexión de red parece funcionar correctamente" in salida


def test_detectar_fallo_dns(capsys, monkeypatch):
    monkeypatch.setattr(
        socket,
        "gethostname",
        lambda: "PC-PRUEBA"
    )

    def resolver_dns(host):
        if host == "PC-PRUEBA":
            return "192.168.1.100"

        raise socket.gaierror

    monkeypatch.setattr(
        socket,
        "gethostbyname",
        resolver_dns
    )

    monkeypatch.setattr(
        diagnostico,
        "comprobar_ping",
        lambda: True
    )

    diagnostico.mostrar_info_red()

    salida = capsys.readouterr().out

    assert "Error al resolver DNS" in salida
    assert "problema de DNS" in salida


def test_detectar_fallo_conectividad(capsys, monkeypatch):
    monkeypatch.setattr(
        socket,
        "gethostname",
        lambda: "PC-PRUEBA"
    )

    def resolver_dns(host):
        if host == "PC-PRUEBA":
            return "192.168.1.100"

        return "93.184.216.34"

    monkeypatch.setattr(
        socket,
        "gethostbyname",
        resolver_dns
    )

    monkeypatch.setattr(
        diagnostico,
        "comprobar_ping",
        lambda: False
    )

    diagnostico.mostrar_info_red()

    salida = capsys.readouterr().out

    assert "DNS funcionando" in salida
    assert "No se ha podido comprobar la conectividad exterior" in salida


def test_fallo_ip_local(capsys, monkeypatch):
    monkeypatch.setattr(
        socket,
        "gethostname",
        lambda: "PC-PRUEBA"
    )

    llamadas = 0

    def resolver_dns(host):
        nonlocal llamadas
        llamadas += 1

        if llamadas == 1:
            raise socket.gaierror

        return "93.184.216.34"

    monkeypatch.setattr(
        socket,
        "gethostbyname",
        resolver_dns
    )

    monkeypatch.setattr(
        diagnostico,
        "comprobar_ping",
        lambda: True
    )

    diagnostico.mostrar_info_red()

    salida = capsys.readouterr().out

    assert "No se pudo obtener la IP local" in salida
    assert "DNS funcionando" in salida