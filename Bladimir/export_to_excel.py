import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect('invitados.db')

# Leer los datos de la tabla
df = pd.read_sql_query('SELECT * FROM invitados', conn)

# Exportar a Excel
df.to_excel('invitados.xlsx', index=False)

# Cerrar la conexión
conn.close()
