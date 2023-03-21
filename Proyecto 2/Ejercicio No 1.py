#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:09:49 2023

@author: hiperion
"""

'''
    Ejercicio No 1
        Fichero autos.csv
        Generar una función y utilizar esta para recodificar la variable “país de
        origen” (1, 2, 3) en el dataframe a través de la función apply.
'''

import pandas as pd
'''Se importan las librerias a utilizar'''

data  = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Data - DATA & ANALYTICS/autos.csv',sep=';', index_col=0)
'''Se importa el archivo csv y asigana a la variable data'''

print(data)

def recodificar_pais(data):
    """
        Recodifica la columna *Pais_Origen* del dataFrame recibido como *data*
        cambia los valores del país segun corresponda
        USA     = 1
        Europe  = 2
        otro    = 3
    """
    print('Funcion')
    data['Pais_Origen'] = data['Pais_Origen'].apply(lambda x:
                                  1 if x == 'USA' else(
                                          2 if x == 'Europe' else 3
                                      )
                              )
    print(data)    
    return data

recodificar_pais(data)
