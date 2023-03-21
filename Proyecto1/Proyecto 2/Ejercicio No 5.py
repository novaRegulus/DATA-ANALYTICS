#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:09:41 2023

@author: hiperion
"""

'''
    Ejercicio No 5
        - Crear una función que devuelva un mapa de calor con la correlación
        de todas las variables numéricas (incluye las generadas), para cada
        país.
    
        ● La función debe contar con su respectiva documentación.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
'''Se importan las librerias a utilizar'''

data  = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Data - DATA & ANALYTICS/autos.csv',sep=';', index_col=0)
'''Se importa el archivo csv y asigana a la variable data'''

data['Caballo_De_Fuerza'] = data['Caballo_De_Fuerza'].fillna(data['Caballo_De_Fuerza'].mean())
'''Se da el tratamiento a los datos perdidos de la columan Caballo_De_Fuerza y se remplazan por la media'''

def mapa_calor():
    """
        Genera y muestra el grafico de mapa de color utilizando las columnas *Desplazamiento* y *Aceleracion* del data frame
    """
    print(data)
    fig, ax = plt.subplots(tight_layout = True)
    hist = ax.hist2d(data['Desplazamiento'], data['Aceleracion'])

mapa_calor()


