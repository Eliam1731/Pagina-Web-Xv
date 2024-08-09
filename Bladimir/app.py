from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/verificar', methods=['POST'])
def verificar():
    nombre = request.json.get('nombre')
    conn = sqlite3.connect('invitados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT cantidad_invitados, asistencia FROM invitados WHERE nombre = ?', (nombre,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        cantidad_invitados, asistencia = resultado
        if asistencia != 'Pendiente':
            return jsonify({'error': 'Ya has confirmado tu asistencia.'}), 400
        return jsonify({'cantidad_invitados': cantidad_invitados})
    else:
        return jsonify({'error': 'Nombre no encontrado.'}), 404

@app.route('/confirmar', methods=['POST'])
def confirmar():
    nombre = request.json.get('nombre')
    asistencia = request.json.get('asistencia')
    
    conn = sqlite3.connect('invitados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT asistencia FROM invitados WHERE nombre = ?', (nombre,))
    resultado = cursor.fetchone()
    
    if resultado:
        estado_asistencia = resultado[0]
        if estado_asistencia != 'Pendiente':
            conn.close()
            return jsonify({'error': 'Ya has confirmado tu asistencia.'}), 400
        
        cursor.execute('''
        UPDATE invitados
        SET asistencia = ?
        WHERE nombre = ?
        ''', (asistencia, nombre))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    else:
        conn.close()
        return jsonify({'error': 'Nombre no encontrado.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
