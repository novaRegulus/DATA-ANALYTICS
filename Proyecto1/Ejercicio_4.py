#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:54:35 2023

@author: hiperion
"""

import pandas as pd

data = pd.read_csv('/home/hiperion/Documentos/Data - DATA & ANALYTICS/Proyecto1/Data - Riesgos.csv', index_col=0)

print(data)

print('======================================')
print('======================================')
print('Mostrar por pantalla las dimensiones del DataFrame:', data.shape)
print('======================================')
print('======================================')
print('El número de datos que contiene:')
print(data.size)
print('======================================')
print('======================================')
print('los nombres de sus columnas:')
print(data.columns)
print('======================================')
print('======================================')
print('los nombres de sus filas:')
print(data.index)
print('======================================')
print('======================================')
print('los tipos de datos de las columnas:')
print(data.dtypes)
print('======================================')
print('======================================')
print('mostrar las 10 primeras filas:')
print(data.head(10))
print('======================================')
print('======================================')
print('las 10 últimas filas:')
print(data.tail(10))
print('======================================')
print('======================================')
print('verificar si tiene datos perdidos/nulos:')
print(data.isnull().sum())
print('======================================')
print('======================================')
print('Extraer las 1000 primeras filas y almacenarlas en un contenedor.')
conteiner = data.head(1000)
print(conteiner)