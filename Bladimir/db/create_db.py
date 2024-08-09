import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('invitados.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS invitados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad_invitados INTEGER NOT NULL,
    asistencia TEXT NOT NULL
)
''')

# Confirmar la creación de la tabla
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos y tabla 'invitados' creadas exitosamente.")
