import platform
import socket
import subprocess

def mostrar_info_sistema():
    print("\n=== INFORMACIÓN DEL SISTEMA ===")
    print("Nombre del equipo:", socket.gethostname())
    print("Sistema operativo:", platform.system())
    print("Versión:", platform.release())
    print("Arquitectura:", platform.machine())


def mostrar_info_red():
    print("\n=== INFORMACIÓN DE RED ===")

    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)

    print("Nombre del equipo:", hostname)
    print("IP local:", ip_local)

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

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True
    )

    if resultado.returncode == 0:
        print("Conectividad correcta")
        return True
    else:
        print("No se ha podido contactar con", host)
        return False


def diagnostico_windows():
    if platform.system() != "Windows":
        print("Este diagnóstico solo está disponible en Windows.")
        return

    print("\n=== DIAGNÓSTICO AVANZADO DE WINDOWS ===")

    resultado = subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            "scripts/diagnostico_windows.ps1"
        ],
        text=True
    )

    if resultado.returncode != 0:
        print("Error al ejecutar el diagnóstico de Windows.")