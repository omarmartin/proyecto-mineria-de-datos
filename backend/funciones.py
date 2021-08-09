import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
import seaborn as sns
import pandas as pd
import shutil
import os
import math


def analisis_exploratorio(archivo):
    print("holi")

def mover(ruta):
    if(os.path.isfile(ruta)):
        os.remove(ruta)
    else:
        print('La carpeta no existe.');

def diagnosis(id, radius, texture, perimeter, area, smoothness, compactness, concavity, concave_points, symmetry, fractal):
    diagnosis = 7.3592 + 2.04930*float(radius) - 0.38473*float(texture) + 0.07151*float(perimeter) - 0.03980*float(area) - 76.43227*float(smoothness) + 1.46242*float(compactness) - 8.46870*float(concavity) - 66.82176*float(concave_points) - 16.27824*float(symmetry) + 68.33703*float(fractal)   
    diagnosisH = 1 / (1+ (math.pow(math.exp(1), - diagnosis)))
    if round(diagnosisH) == 0:
        mensaje = 'El paciente ' + id + '. Diagnóstico es 0 o Maligno'
    else:
        mensaje = 'El paciente ' + id + '. Diagnóstico es 1 o Benigno'
    return mensaje

