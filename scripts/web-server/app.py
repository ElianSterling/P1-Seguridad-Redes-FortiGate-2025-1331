import os
import pymysql

from flask import Flask, render_template_string, request
from dotenv import load_dotenv

load_dotenv("/etc/p1-webapp.env")

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def index():
    connection = get_db()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, nombre, descripcion, precio FROM productos"
            )
            productos = cursor.fetchall()
    finally:
        connection.close()

    return render_template_string("""
    <html>
    <head><title>P1 - Seguridad de Redes</title></head>
    <body>
        <h1>WEB01 - Aplicación HTTPS</h1>
        <p>Datos obtenidos desde DB01 mediante TCP/3306.</p>

        <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Producto</th>
                <th>Descripción</th>
                <th>Precio</th>
            </tr>
            {% for p in productos %}
            <tr>
                <td>{{ p.id }}</td>
                <td>{{ p.nombre }}</td>
                <td>{{ p.descripcion }}</td>
                <td>${{ p.precio }}</td>
            </tr>
            {% endfor %}
        </table>

        <p>Laboratorio autorizado de detección SQL Injection.</p>
    </body>
    </html>
    """, productos=productos)

@app.route("/buscar")
def buscar():
    producto_id = request.args.get("id", "1")

    connection = get_db()

    try:
        with connection.cursor() as cursor:
            # INTENCIONALMENTE VULNERABLE PARA EL LABORATORIO
            query = f"""
                SELECT id, nombre, descripcion, precio
                FROM productos
                WHERE id = {producto_id}
            """
            cursor.execute(query)
            productos = cursor.fetchall()
    finally:
        connection.close()

    return render_template_string("""
    <html>
    <head><title>Prueba SQLi - P1</title></head>
    <body>
        <h1>Búsqueda de productos</h1>

        <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Producto</th>
                <th>Descripción</th>
                <th>Precio</th>
            </tr>
            {% for p in productos %}
            <tr>
                <td>{{ p.id }}</td>
                <td>{{ p.nombre }}</td>
                <td>{{ p.descripcion }}</td>
                <td>${{ p.precio }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """, productos=productos)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
