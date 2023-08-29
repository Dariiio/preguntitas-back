import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
db_name = "preguntitas.db"


class PreguntaDB:
    def __enter__(self):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

    def crear_tabla(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS preguntas (
                                id INTEGER PRIMARY KEY,
                                texto TEXT,
                                categoria TEXT
                            )"""
        )

    def insertar_pregunta(self, texto, categoria):
        self.cursor.execute(
            "INSERT INTO preguntas (texto, categoria) VALUES (?, ?)", (texto, categoria)
        )

    def obtener_preguntas(self):
        self.cursor.execute("SELECT * FROM preguntas")
        return self.cursor.fetchall()

    def actualizar_pregunta(self, id, nuevo_texto, nueva_categoria):
        self.cursor.execute(
            "UPDATE preguntas SET texto = ?, categoria = ? WHERE id = ?",
            (nuevo_texto, nueva_categoria, id),
        )

    def eliminar_pregunta(self, id):
        self.cursor.execute("DELETE FROM preguntas WHERE id = ?", (id,))

    def obtener_pregunta_aleatoria(self):
        self.cursor.execute("SELECT * FROM preguntas ORDER BY RANDOM() LIMIT 1")
        pregunta = self.cursor.fetchone()
        return pregunta


@app.route("/preguntas", methods=["GET"])
def obtener_todas_las_preguntas():
    with PreguntaDB() as db:
        preguntas = db.obtener_preguntas()
        return jsonify(preguntas)


@app.route("/preguntas", methods=["POST"])
def crear_pregunta():
    datos = request.get_json()
    texto = datos.get("texto")
    categoria = datos.get("categoria")

    if texto and categoria:
        with PreguntaDB() as db:
            db.insertar_pregunta(texto, categoria)
        return "Pregunta creada exitosamente", 201
    else:
        return "Faltan datos en la solicitud", 400


@app.route("/preguntas/<int:id>", methods=["PUT"])
def actualizar_pregunta(id):
    datos = request.get_json()
    nuevo_texto = datos.get("texto")
    nueva_categoria = datos.get("categoria")

    if nuevo_texto and nueva_categoria:
        with PreguntaDB() as db:
            db.actualizar_pregunta(id, nuevo_texto, nueva_categoria)
        return "Pregunta actualizada exitosamente", 200
    else:
        return "Faltan datos en la solicitud", 400


@app.route("/preguntas/<int:id>", methods=["DELETE"])
def eliminar_pregunta(id):
    with PreguntaDB() as db:
        db.eliminar_pregunta(id)
        return "Pregunta eliminada exitosamente", 200


@app.route("/preguntas/random", methods=["GET"])
def obtener_pregunta_aleatoria():
    with PreguntaDB() as db:
        pregunta = db.obtener_pregunta_aleatoria()
        if pregunta:
            return jsonify(
                {"id": pregunta[0], "texto": pregunta[1], "categoria": pregunta[2]}
            )
        else:
            return "No hay preguntas en la base de datos", 404


if __name__ == "__main__":
    with PreguntaDB() as db:
        db.crear_tabla()

    app.run(debug=True)
