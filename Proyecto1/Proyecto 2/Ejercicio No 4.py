#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:09:17 2023

@author: hiperion
"""

'''
    Ejercicio No 4
        - Crear una función que muestre los siguientes gráficos
        (simultáneamente) para las variables numéricas, según una variable
        cualitativa:
    
        ❖ Cajas y bigotes
        ❖ Barras de la media
        ❖ Histograma con densidad (Curva)
        
        La función debe contar con su respectiva documentación.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
'''Se importan las librerias a utilizar'''

data  = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Data - DATA & ANALYTICS/autos.csv',sep=';', index_col=0)
'''Se importa el archivo csv y asigana a la variable data'''

def caja_bigotes():
    """
        Mediante la función boxplot de la libreria seaborn, utilizando la variable sns,
        se genera y muestra la grafica de Caja y Bigotes
    """
    ax = sns.boxplot(data  = data)
    plt.show()


def barra_media():
    """
        Mediante la función barplot de la libreria seaborn, utilizando la variable sns,
        se genera y muestra la grafica de Barras de la Media
    """
    sns.barplot(x = "Cilindros", y = "Desplazamiento", data = data)
    plt.show()


def histograma_den():
    """
        Mediante la función histplot de la libreria seaborn, utilizando la variable sns,
        se genera y muestra la grafica de Histograma con densidad 
    """
    sns.histplot(data  = data['Cilindros'], kde = True)
    plt.show()

#Se llaman a las funciones para ser utilizadas    
caja_bigotes()
barra_media()
histograma_den()