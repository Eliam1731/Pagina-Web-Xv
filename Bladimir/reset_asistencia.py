import sqlite3

def reset_asistencia():
    conn = sqlite3.connect('invitados.db')
    cursor = conn.cursor()
    
    # Actualiza todos los registros para poner la asistencia como 'Pendiente'
    cursor.execute('''
    UPDATE invitados
    SET asistencia = 'Pendiente'
    ''')

    conn.commit()
    conn.close()
    print("Todos los registros han sido actualizados a 'Pendiente'.")

if __name__ == '__main__':
    reset_asistencia()
