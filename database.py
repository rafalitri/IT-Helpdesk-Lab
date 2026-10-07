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