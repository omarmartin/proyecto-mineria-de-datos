from backend.funciones import mover
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import csv, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shutil
from os import remove
from os import path



app = Flask(__name__)
CORS(app)

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos'

#archivo = pd.read_csv('./Archivos/melb_data.csv')
archivo = pd.read_csv('./Archivos/WDBCOriginal.csv')


csvjson = 'hola'

@app.route('/reglas_asociacion', methods = ['GET','POST'])
def reglas():
    if request.method == 'POST':
        data = json.loads(request.data)
        support = data["support"]
        confidence = data["confidence"]
        lift = data["lift"]      
        lista = []
        print(support)
        print(confidence)
        print(lift)
    lista.append(support)
    lista.append(confidence)
    lista.append(lift)
    print(lista)
    return jsonify(lista)


@app.route('/correlaciones', methods = ['GET'])
def correlaciones():
    mover("./frontend/public/image/correlacion_pearson.png")
    plt.figure(figsize=(10,10))
    sns.heatmap(archivo.corr(), cmap='RdBu_r', annot=True)
    rutaCrear = "./frontend/public/imagetemp/correlacion_pearson.png"
    rutaMover =  "./frontend/public/image/correlacion_pearson.png"
    plt.savefig(rutaCrear)
    shutil.move(rutaCrear, rutaMover)
    plt.clf()
    return "hola"

def borrarImagenes(ruta):
    try:
        os.remove(ruta)
        os.mkdir(ruta)
    except: 
        print("")

@app.route('/datos_header', methods = ['GET'])
def get_headers():
  try:
    return [{'text': str(data), 'value': str(data), 'sortable': False} for data in archivo]
  except:
    pass

@app.route('/datos_table', methods = ['GET'])
def get_table():
  global registros
  try:
    df1 = archivo.where(pd.notnull(archivo), None)
    registros = json.loads(df1.to_json(orient='records'))
    return registros
  except:
    pass

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
