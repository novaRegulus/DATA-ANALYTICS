#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:12:25 2023

@author: hiperion
"""

'''
    Ejercicio No 2
        Generar un Notebook Colab con código y resultados, que contiene
        información de autos de un periodo de tiempo. Resolver los siguientes:
        - Limpieza y tratamiento de las variables (Según corresponda)
        - Generar 5 nuevas variables aplicando los siguientes criterios con las
        variables numéricas:
        
        1. Log10(var1/var2)
        2. Sqrt(var1)*exp(var2)/200
        
        3. Si var 1 > var 2 → 5, caso contrario 3
        4. 1/logn(var1/var2)*100
        5. var2**2/var1
'''

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
'''Se importan las librerias a utilizar'''

data  = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Data - DATA & ANALYTICS/autos.csv',sep=';', index_col=0)
'''Se importa el archivo csv y asigana a la variable data'''

a1 = data[:][data["Anyo"] == "1/01/1970"] 

print(a1)


def getData():
    """
        Genera cinco nuevas columnas del dataframe
        COL-1 = Log10(var1/var2)
        Col-2 = Sqrt(var1)*exp(var2)/200
        Col-3 = Si var 1 > var 2 → 5, caso contrario 3
        Col-4 = 1/logn(var1/var2)*100
        Col-5 = var2**2/var1
    """
    data['COL-1'] = np.log10(data.Desplazamiento * data.Aceleracion)
    data['COL-2'] = np.sqrt(data.Desplazamiento) * np.exp(data.Aceleracion) / 200
    data['COL-3'] = np.where(data.Desplazamiento > data.Aceleracion, 5, 3)
    data['COL-4'] = 1/np.log(data.Desplazamiento, data.Aceleracion) * 100
    data['COL-5']  = data.Aceleracion**2 / data.Desplazamiento
    #======Ejercicio No 5=========
    df1 = data.drop(['Pais_Origen', 'Nombre', 'Anyo'], axis = 1)
    mapa = sns.heatmap(df1)


    
getData()   

print(data) 
