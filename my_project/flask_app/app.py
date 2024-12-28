from flask import Flask, jsonify, send_from_directory
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',  # Имя сервиса базы данных из docker-compose
        database='mydatabase',
        user='myuser',
        password='mypassword'
    )
    return conn

@app.route('/')
def index():
    return "Welcome to the Flask application!"  # Простой маршрут для корня

@app.route('/users', methods=['GET'])
def users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        users_list = [{'id': user[0], 'name': user[1]} for user in users]
        return jsonify(users_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/front/<path:filename>')
def serve_frontend(filename):
    return send_from_directory('front', filename)  # Обслуживание статических файлов из папки 'front'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

