import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
import seaborn as sns
import pandas as pd
import shutil
import os


def analisis_exploratorio(archivo):
    print("holi")

def mover(ruta):
    if(os.path.isfile(ruta)):
        os.remove(ruta)
    else:
        print('La carpeta no existe.');
