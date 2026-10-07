import requests


def obtener_datos_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        respuesta = requests.get(
            url,
            timeout=5
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        print("Código HTTP:", respuesta.status_code)
        print("Datos recibidos:")
        print(datos)

    except requests.exceptions.Timeout:
        print("La API ha tardado demasiado en responder.")

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con la API.")

    except requests.exceptions.HTTPError as error:
        print("La API devolvió un error HTTP:", error)

    except requests.exceptions.RequestException as error:
        print("Error al realizar la petición:", error)


def crear_tarea_api():
    url = "https://jsonplaceholder.typicode.com/todos"

    nueva_tarea = {
        "userId": 1,
        "title": "Revisar incidencia de red",
        "completed": False
    }

    respuesta = requests.post(
        url,
        json=nueva_tarea,
        timeout=5
    )

    print("Código HTTP:", respuesta.status_code)

    datos = respuesta.json()

    print("Respuesta de la API:")
    print(datos)


def actualizar_tarea_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    cambios = {
        "completed": True
    }

    respuesta = requests.patch(
        url,
        json=cambios,
        timeout=5
    )

    print("Código HTTP:", respuesta.status_code)

    datos = respuesta.json()

    print("Tarea actualizada:")
    print(datos)

def eliminar_tarea_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    respuesta = requests.delete(
        url,
        timeout=5
    )

    print("Código HTTP:", respuesta.status_code)

    if respuesta.status_code == 200:
        print("Tarea eliminada correctamente")
    else:
        print("No se pudo eliminar la tarea")