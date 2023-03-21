#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:08:15 2023

@author: hiperion
"""

'''
    Ejercicio No 3
        - Crear una función que permita generar 3 variables cualitativas
        ordinales a partir de las variables numéricas con los siguientes criterios:
            ★ Si es mayor a la “media + 1*desviación estándar” → Alto
            ★ Si está entre “media - 1*desviación estándar” y “media +
            1*desviación estándar” → Medio
            ★ Si es menor a la “media - 1*desviación estándar” → Bajo
        Nota: Mostrar con las nuevas variables generadas.
        Elegir con libertad las variables a trabajar.
        La función debe contar con su respectiva documentación.
'''

import pandas as pd
import numpy as np
'''Se importan las librerias a utilizar'''

data  = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Data - DATA & ANALYTICS/autos.csv',sep=';', index_col=0)
'''Se importa el archivo csv y asigana a la variable data'''

media = data['Desplazamiento'].median()
desviacion_standar = data['Desplazamiento'].std()
'''Se calcula la media y variación estandar de la columna Desplazamiento'''

alto = media + 1 * desviacion_standar
medio1 = media - (1 * desviacion_standar)
medio2 = media - (1 * desviacion_standar)
bajo = media - (1 * desviacion_standar)
'''Se calcula con valores numericos los valores para las variables Alto, Medio y Bajo'''

def generar_variables(data):
    """
        Recibe como parametro el dataFrame
        genera una lista de condiciones para la columna Desplazamiento con los valores Alto, Medio y Bajo
        genera una lista de valores 'Alto', 'Medio', 'Bajo'
        Se agrega la columna 'Status', con la fucnión de numpy 'select' se va a asignar la lista de valores
        segun las condicones referidas para cada valor, por defecto se asigna Bajo
    
    """
    condition_list = [
        (data.Desplazamiento >= alto),
        ((data.Desplazamiento >= medio1) & (data.Desplazamiento < medio2)),
        (data.Desplazamiento < bajo)
    ]
    choice_list = ['Alto', 'Medio', 'Bajo']
    data['Status'] = np.select(condition_list, choice_list, default='Bajo')
    #return data


generar_variables(data)
print(data)


