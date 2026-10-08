# IT Helpdesk Lab

IT Helpdesk Lab es un proyecto que he ido desarrollando en Python para practicar y refrescar conocimientos relacionados con soporte técnico, sistemas, redes, SQL y automatización.

Empezó como una aplicación sencilla para registrar incidencias desde terminal y poco a poco fui añadiendo una base de datos, gestión de técnicos, consultas SQL, diagnósticos de Windows, PowerShell, una API REST y tests automatizados.

La idea ha sido ir ampliándolo poco a poco mientras practicaba también Git y GitHub durante el desarrollo.

## Funcionalidades

### Gestión de incidencias

La aplicación permite:

- Crear incidencias.
- Ver las incidencias existentes.
- Cerrar incidencias.
- Consultar incidencias pendientes.
- Guardar la información en una base de datos SQLite.
- Registrar determinadas acciones mediante logging.

Cada incidencia tiene:

- ID.
- Usuario.
- Descripción del problema.
- Estado.

## Gestión de técnicos

También se pueden gestionar técnicos desde el propio programa:

- Crear técnicos.
- Ver los técnicos registrados.
- Asignar un técnico a una incidencia.
- Cambiar la asignación de una incidencia.
- Consultar las incidencias junto con el técnico asignado.

Si una incidencia todavía no tiene técnico, se muestra como:

```text
SIN ASIGNAR
```

## Base de datos y SQL

Para almacenar la información utilizo SQLite.

Actualmente la base de datos contiene tres tablas principales:

```text
incidencias
tecnicos
asignaciones
```

Durante el desarrollo he trabajado con consultas y conceptos SQL como:

```text
SELECT
INSERT
UPDATE
DELETE
WHERE
ORDER BY
COUNT
GROUP BY
FOREIGN KEY
INNER JOIN
LEFT JOIN
```

Por ejemplo, las tablas `incidencias` y `tecnicos` se relacionan mediante la tabla `asignaciones`.

## Diagnóstico del sistema

El programa incluye varias funciones de diagnóstico para obtener información básica del equipo:

- Nombre del equipo.
- Sistema operativo.
- Versión.
- Arquitectura.
- Dirección IP.
- Resolución DNS.
- Prueba de conectividad mediante ping.

## Diagnóstico de Windows con PowerShell

También añadí un script de PowerShell para obtener información más detallada de equipos Windows.

El script comprueba:

- Sistema operativo.
- Uso de memoria RAM.
- Espacio disponible en discos.
- Procesos con mayor consumo de memoria.
- Adaptadores de red.
- Direcciones IPv4.
- Puerta de enlace.
- Servidores DNS.
- Estado de los servicios DHCP y DNS.

El script se encuentra en:

```text
scripts/diagnostico_windows.ps1
```

y puede ejecutarse directamente desde el menú de la aplicación.

## API REST

El proyecto incluye un pequeño cliente HTTP utilizando la librería `requests`.

He utilizado una API pública de pruebas para trabajar con los principales métodos HTTP:

```text
GET
POST
PATCH
DELETE
```

También he añadido manejo de errores para situaciones como:

- Timeout.
- Problemas de conexión.
- Errores HTTP.
- Otros errores de `requests`.

Para las pruebas utilizo JSONPlaceholder.

## Tests

El proyecto utiliza `pytest`.

Actualmente hay tests para:

- Gestión de incidencias.
- Gestión de técnicos.
- Base de datos.
- Consultas SQL.
- Asignación de técnicos.
- Diagnóstico del sistema.
- Cliente API.
- Errores HTTP y problemas de conexión.

También utilizo herramientas de pytest como:

```text
monkeypatch
capsys
tmp_path
```

Esto permite hacer pruebas sin modificar la base de datos real y sin depender de una conexión real a Internet.

Actualmente:

```text
22 tests passed
```

## Tecnologías utilizadas

- Python
- SQLite
- SQL
- PowerShell
- Requests
- Pytest
- Git
- GitHub
- HTTP / REST
- JSON
- TCP/IP

## Estructura del proyecto

```text
IT-Helpdesk-Lab/
│
├── scripts/
│   └── diagnostico_windows.ps1
│
├── tests/
│   ├── test_api_client.py
│   ├── test_database.py
│   ├── test_diagnostico.py
│   └── test_incidencias.py
│
├── api_client.py
├── database.py
├── diagnostico.py
├── incidencias.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/rafalitri/IT-Helpdesk-Lab.git
```

Entrar en la carpeta:

```bash
cd IT-Helpdesk-Lab
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar el programa

```bash
python main.py
```

El programa muestra actualmente el siguiente menú:

```text
=== IT HELPDESK LAB ===

1. Crear incidencia
2. Ver incidencias
3. Cerrar incidencia
4. Diagnóstico del sistema
5. Diagnóstico de red
6. Diagnóstico avanzado de Windows
7. Consultar API
8. Ver incidencias con técnico
9. Crear técnico
10. Ver técnicos
11. Asignar técnico a incidencia
12. Salir
```

## Ejecutar los tests

```bash
python -m pytest
```

## Archivos locales

La base de datos y los logs se crean de forma local:

```text
helpdesk.db
helpdesk.log
```

Estos archivos no se suben al repositorio.

También se ignoran:

```text
.venv/
.pytest_cache/
__pycache__/
```

## Sobre el proyecto

He creado este proyecto principalmente para volver a trabajar de forma práctica con Python y recuperar soltura después de un tiempo sin programar tanto.

En lugar de hacer ejercicios separados, he preferido ir construyendo una misma aplicación e ir añadiendo cosas según avanzaba: primero incidencias, después SQLite, tests, diagnósticos, APIs y finalmente relaciones entre tablas y gestión de técnicos.

También me ha servido para acostumbrarme de nuevo a trabajar con ramas, commits y Pull Requests en GitHub.

## Autor

**Rafael Parra**

GitHub: [rafalitri](https://github.com/rafalitri)