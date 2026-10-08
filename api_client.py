import requests


def hacer_peticion(metodo, url, **kwargs):
    try:
        respuesta = requests.request(
            metodo,
            url,
            timeout=5,
            **kwargs
        )

        respuesta.raise_for_status()

        return respuesta

    except requests.exceptions.Timeout:
        print("La API ha tardado demasiado en responder.")

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con la API.")

    except requests.exceptions.HTTPError as error:
        print("La API devolvió un error HTTP:", error)

    except requests.exceptions.RequestException as error:
        print("Error al realizar la petición:", error)

    return None


def obtener_datos_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    respuesta = hacer_peticion(
        "GET",
        url
    )

    if respuesta is None:
        return

    datos = respuesta.json()

    print("Código HTTP:", respuesta.status_code)
    print("Datos recibidos:")
    print(datos)


def crear_tarea_api():
    url = "https://jsonplaceholder.typicode.com/todos"

    nueva_tarea = {
        "userId": 1,
        "title": "Revisar incidencia de red",
        "completed": False
    }

    respuesta = hacer_peticion(
        "POST",
        url,
        json=nueva_tarea
    )

    if respuesta is None:
        return

    datos = respuesta.json()

    print("Código HTTP:", respuesta.status_code)
    print("Respuesta de la API:")
    print(datos)


def actualizar_tarea_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    cambios = {
        "completed": True
    }

    respuesta = hacer_peticion(
        "PATCH",
        url,
        json=cambios
    )

    if respuesta is None:
        return

    datos = respuesta.json()

    print("Código HTTP:", respuesta.status_code)
    print("Tarea actualizada:")
    print(datos)


def eliminar_tarea_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    respuesta = hacer_peticion(
        "DELETE",
        url
    )

    if respuesta is None:
        return

    print("Código HTTP:", respuesta.status_code)
    print("Tarea eliminada correctamente")