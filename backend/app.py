from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import csv, json
import pandas as pd

app = Flask(__name__)
CORS(app)

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos'

archivo = pd.read_csv("D:/flask/proyecto/Archivos/WDBCOriginal.csv")



@app.route('/datos_headers', methods = ['GET'])
def get_table():
   # with the delimiter as ,
    csv_reader = pd.read_csv("D:/flask/proyecto/Archivos/WDBCOriginal.csv")
    file = pd.DataFrame(csv_reader)
    result = file.to_json(orient= "split")
    return  result
        


@app.route('/datos_table', methods = ['GET'])
def get_headers():
    csv_reader = pd.read_csv("D:/flask/proyecto/Archivos/WDBCOriginal.csv")
    file = pd.DataFrame(csv_reader)
    result = file.to_json(orient= "records")
    parsed = json.loads(result)
    return jsonify(json.dumps(parsed, indent=4))

@app.route("/", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        archivo
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria
        return "/home"

@app.route('/datos', methods = ['GET'])
def get_csv():
    data = {}
    csvReader = csv.DictReader(archivo)
    i = 0
    for rows in csvReader:
        data[i] = rows
        i += 1
    i=0
    print(jsonify(data))
    return jsonify(data)


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

