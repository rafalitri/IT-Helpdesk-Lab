import platform
import socket
import subprocess
from pathlib import Path


def mostrar_info_sistema():
    print("\n=== INFORMACIÓN DEL SISTEMA ===")
    print("Nombre del equipo:", socket.gethostname())
    print("Sistema operativo:", platform.system())
    print("Versión:", platform.release())
    print("Arquitectura:", platform.machine())


def mostrar_info_red():
    print("\n=== INFORMACIÓN DE RED ===")

    hostname = socket.gethostname()

    print("Nombre del equipo:", hostname)

    try:
        ip_local = socket.gethostbyname(hostname)
        print("IP local:", ip_local)

    except socket.gaierror:
        print("No se pudo obtener la IP local")

    try:
        ip_dns = socket.gethostbyname("example.com")
        print("DNS funcionando:", ip_dns)
        dns_funciona = True

    except socket.gaierror:
        print("Error al resolver DNS")
        dns_funciona = False

    ping_funciona = comprobar_ping()

    print("\n=== DIAGNÓSTICO ===")

    if ping_funciona and dns_funciona:
        print("La conexión de red parece funcionar correctamente.")

    elif ping_funciona and not dns_funciona:
        print("Hay conectividad, pero parece existir un problema de DNS.")

    else:
        print("No se ha podido comprobar la conectividad exterior.")


def comprobar_ping(host="8.8.8.8"):
    print("\n=== PRUEBA DE CONECTIVIDAD ===")
    print("Probando conexión con:", host)

    if platform.system() == "Windows":
        comando = ["ping", "-n", "1", host]
    else:
        comando = ["ping", "-c", "1", host]

    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            timeout=5
        )

    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("No se pudo ejecutar la prueba de ping.")
        return False

    if resultado.returncode == 0:
        print("Conectividad correcta")
        return True

    print("No se ha podido contactar con", host)
    return False


def diagnostico_windows():
    if platform.system() != "Windows":
        print("Este diagnóstico solo está disponible en Windows.")
        return

    print("\n=== DIAGNÓSTICO AVANZADO DE WINDOWS ===")

    ruta_script = (
        Path(__file__).parent
        / "scripts"
        / "diagnostico_windows.ps1"
    )

    if not ruta_script.exists():
        print("No se encontró el script de diagnóstico de Windows.")
        return

    resultado = subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(ruta_script)
        ],
        text=True
    )

    if resultado.returncode != 0:
        print("Error al ejecutar el diagnóstico de Windows.")