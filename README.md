# IT Helpdesk Lab

Proyecto práctico de soporte IT desarrollado en Python para reforzar conocimientos de programación, sistemas, redes, bases de datos, testing y automatización con PowerShell.

La aplicación permite gestionar incidencias y ejecutar diferentes herramientas de diagnóstico sobre el equipo y la red.

## Funcionalidades

### Gestión de incidencias

- Crear incidencias.
- Listar incidencias.
- Cerrar incidencias por ID.
- IDs generados automáticamente.
- Persistencia mediante SQLite.
- Registro de eventos mediante logging.

### Diagnóstico del sistema

La aplicación puede mostrar:

- Nombre del equipo.
- Sistema operativo.
- Versión del sistema.
- Arquitectura.

### Diagnóstico de red

Permite comprobar:

- Dirección IP local.
- Resolución DNS.
- Conectividad mediante ping.
- Detección básica de posibles problemas DNS o de conectividad.

### Diagnóstico avanzado de Windows

El proyecto incluye un script PowerShell que permite consultar:

- Sistema operativo.
- Memoria RAM total, usada y libre.
- Porcentaje de uso de RAM.
- Espacio disponible en discos.
- Avisos por poco espacio disponible.
- Procesos con mayor consumo de memoria.
- Adaptadores de red.
- Direcciones IPv4.
- Puerta de enlace.
- Servidores DNS.
- Estado de los servicios DHCP y Cliente DNS.

El diagnóstico PowerShell puede ejecutarse desde la propia aplicación Python.

## Tecnologías utilizadas

- Python
- SQLite
- SQL
- PowerShell
- Git
- GitHub
- pytest
- Logging
- Redes TCP/IP

## Estructura del proyecto

```text
IT-Helpdesk-Lab/
│
├── main.py
├── incidencias.py
├── database.py
├── diagnostico.py
├── requirements.txt
├── README.md
│
├── scripts/
│   └── diagnostico_windows.ps1
│
└── tests/
    ├── test_database.py
    ├── test_diagnostico.py
    └── test_incidencias.py
```

Los archivos generados localmente como la base de datos, logs, cachés y el entorno virtual están excluidos mediante `.gitignore`.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/rafalitri/IT-Helpdesk-Lab.git
cd IT-Helpdesk-Lab
```

Crear un entorno virtual:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Ejecución

Ejecutar la aplicación:

```powershell
python main.py
```

El programa mostrará un menú similar a:

```text
=== IT HELPDESK LAB ===
1. Crear incidencia
2. Ver incidencias
3. Cerrar incidencia
4. Diagnóstico del sistema
5. Diagnóstico de red
6. Diagnóstico avanzado de Windows
7. Salir
```

La base de datos SQLite se crea automáticamente la primera vez que se ejecuta la aplicación.

## Tests

El proyecto utiliza `pytest` para realizar pruebas automáticas.

Para ejecutar todos los tests:

```powershell
python -m pytest
```

Los tests comprueban, entre otras cosas:

- Creación y gestión de incidencias.
- Operaciones CRUD de SQLite.
- Incidencias pendientes y resueltas.
- IDs incorrectos.
- Fallos de DNS simulados.
- Fallos de conectividad simulados.

Las pruebas utilizan archivos y datos temporales para evitar modificar la base de datos real.

## Logging

La aplicación registra eventos importantes en:

```text
helpdesk.log
```

Por ejemplo:

```text
INFO - Nueva incidencia creada
INFO - Incidencia cerrada
WARNING - Se intentó cerrar un ID inexistente
```

El archivo de log es local y no se almacena en GitHub.

## Objetivo del proyecto

Este proyecto ha sido creado como laboratorio práctico para trabajar conceptos relacionados con:

- Helpdesk y soporte técnico.
- Administración de sistemas.
- Diagnóstico de equipos.
- Redes.
- Python.
- PowerShell.
- SQL y bases de datos.
- Testing automático.
- Git y GitHub.

El objetivo es seguir ampliándolo progresivamente con nuevas herramientas de administración y automatización.