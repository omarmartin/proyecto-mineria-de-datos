from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos'


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria
        return "subido correctamente"

@app.route('/get', methods = ['GET'])
def get_articles():
    return jsonify({
        "id": "1",
        "nombre": "juan"
    },
    {
        "id":"2",
        "nombre": "john"
    })


if __name__ == "__main__":
    app.rin(debug=True)
