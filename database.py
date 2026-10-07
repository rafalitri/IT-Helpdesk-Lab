import sqlite3


DATABASE = "helpdesk.db"


def crear_tabla():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS incidencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            problema TEXT NOT NULL,
            resuelta INTEGER NOT NULL DEFAULT 0
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tecnicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS asignaciones (
            incidencia_id INTEGER NOT NULL,
            tecnico_id INTEGER NOT NULL,
            FOREIGN KEY (incidencia_id) REFERENCES incidencias(id),
            FOREIGN KEY (tecnico_id) REFERENCES tecnicos(id)
        )
        """
    )

    conexion.commit()
    conexion.close()


def insertar_incidencia(usuario, problema):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO incidencias (usuario, problema)
        VALUES (?, ?)
        """,
        (usuario, problema)
    )

    conexion.commit()
    conexion.close()


def obtener_incidencias():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT id, usuario, problema, resuelta
        FROM incidencias
        ORDER BY id
        """
    )

    incidencias = cursor.fetchall()

    conexion.close()

    return incidencias


def obtener_incidencias_pendientes():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT id, usuario, problema, resuelta
        FROM incidencias
        WHERE resuelta = 0
        ORDER BY id
        """
    )

    incidencias = cursor.fetchall()

    conexion.close()

    return incidencias


def contar_incidencias_pendientes():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM incidencias
        WHERE resuelta = 0
        """
    )

    cantidad = cursor.fetchone()[0]

    conexion.close()

    return cantidad


def contar_incidencias_por_estado():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT resuelta, COUNT(*)
        FROM incidencias
        GROUP BY resuelta
        ORDER BY resuelta
        """
    )

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


def cerrar_incidencia_db(id_incidencia):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE incidencias
        SET resuelta = 1
        WHERE id = ?
        """,
        (id_incidencia,)
    )

    encontrada = cursor.rowcount > 0

    conexion.commit()
    conexion.close()

    return encontrada


def eliminar_incidencia_db(id_incidencia):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        DELETE FROM incidencias
        WHERE id = ?
        """,
        (id_incidencia,)
    )

    eliminada = cursor.rowcount > 0

    conexion.commit()
    conexion.close()

    return eliminada


def insertar_tecnico(nombre):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO tecnicos (nombre)
        VALUES (?)
        """,
        (nombre,)
    )

    conexion.commit()
    conexion.close()


def asignar_tecnico(incidencia_id, tecnico_id):
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO asignaciones (incidencia_id, tecnico_id)
        VALUES (?, ?)
        """,
        (incidencia_id, tecnico_id)
    )

    conexion.commit()
    conexion.close()


def obtener_incidencias_con_tecnico():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT
            incidencias.id,
            incidencias.usuario,
            incidencias.problema,
            tecnicos.nombre
        FROM incidencias
        INNER JOIN asignaciones
            ON incidencias.id = asignaciones.incidencia_id
        INNER JOIN tecnicos
            ON asignaciones.tecnico_id = tecnicos.id
        ORDER BY incidencias.id
        """
    )

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


def obtener_todas_incidencias_con_tecnico():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT
            incidencias.id,
            incidencias.usuario,
            incidencias.problema,
            tecnicos.nombre
        FROM incidencias
        LEFT JOIN asignaciones
            ON incidencias.id = asignaciones.incidencia_id
        LEFT JOIN tecnicos
            ON asignaciones.tecnico_id = tecnicos.id
        ORDER BY incidencias.id
        """
    )

    resultados = cursor.fetchall()

    conexion.close()

    return resultados