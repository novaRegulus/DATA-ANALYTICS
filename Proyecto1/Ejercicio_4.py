#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:54:35 2023

@author: hiperion
"""

import pandas as pd

data = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Proyecto1/Data - Riesgos.csv', index_col=0)
'''
    Se importa el archivo Data - Riesgos.csv y se asigna a una variable data
'''
print('======================================')
print('======================================')
'''
    Se mustra las simenciones del dataFrame
'''
print('Mostrar por pantalla las dimensiones del DataFrame:', data.shape)
print('======================================')
print('======================================')
print('El número de datos que contiene:')
print(data.size)
'''
    Se mustra el número de datos que contiene el dataFrame
'''
print('======================================')
print('======================================')
print('los nombres de sus columnas:')
print(data.columns)
'''
    Se mustra los nombres de sus columnas del dataFrame
'''
print('======================================')
print('======================================')
print('los nombres de sus filas:')
print(data.index)
'''
    Se mustra los nombres de sus filas del dataFrame
'''
print('======================================')
print('======================================')
print('los tipos de datos de las columnas:')
print(data.dtypes)
'''
    Se mustra los tipos de datos de las columnas del dataFrame
'''
print('======================================')
print('======================================')
print('mostrar las 10 primeras filas:')
print(data.head(10))
'''
    Se mustra las 10 primeras filas del dataFrame
'''
print('======================================')
print('======================================')
print('las 10 últimas filas:')
print(data.tail(10))
'''
    Se mustra las 10 últimas filas del dataFrame
'''
print('======================================')
print('======================================')
print('verificar si tiene datos perdidos/nulos:')
print(data.isnull().sum())
'''
    Se mustra el total de los datos perdidos/nulos por columas del dataFrame
'''
print('======================================')
print('======================================')
print('Extraer las 1000 primeras filas y almacenarlas en un contenedor.')
conteiner = data.head(1000)
'''
    Se Extraer las 1000 primeras filas y almacenan en un contenedor
'''
print(conteiner)