import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('invitados.db')
cursor = conn.cursor()

# Datos iniciales (puedes añadir tantos como necesites)
datos_iniciales = [
    ('Luis Fernando', 2),
    ('Lucas Dalto', 3),
    ('Carlos Fernandez', 4),
    ('Eliam Jimenez', 2)
]

# Insertar datos iniciales
for nombre, cantidad_invitados in datos_iniciales:
    cursor.execute('''
    INSERT INTO invitados (nombre, cantidad_invitados, asistencia) 
    VALUES (?, ?, ?)
    ''', (nombre, cantidad_invitados, 'Pendiente'))

# Confirmar la inserción de datos
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos iniciales agregados exitosamente.")
