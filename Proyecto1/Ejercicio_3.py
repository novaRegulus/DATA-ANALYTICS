#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:43:09 2023

@author: hiperion
"""


import pandas as pd
import numpy as np

data = { 'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'], 'Ventas': [30500, 35600, 28300, 33900, 42500], 'Gastos': [22000, 23450, 18100, 35700, 32450] }
dataFrame = pd.DataFrame(data)
print(dataFrame)
print('======================================')
print('======================================')
dataFrame['Columna 1'] = dataFrame.Gastos / dataFrame.Ventas * 100
print(dataFrame)
print('======================================')
print('======================================')
dataFrame['Columna 2'] = np.where(dataFrame['Ventas'] >= 30000, 'Meta Superada', 'Meta no Superada')
print('======================================')
print('======================================')
print(dataFrame)
dataFrame['Columna 3'] = dataFrame.Gastos - dataFrame.Ventas
print('======================================')
print('======================================')
print(dataFrame)
print('======================================')
print('======================================')
meses = ['Marzo', 'Abril', 'Mayo']
dataventas_totales = dataFrame.set_index('Mes').loc[meses].sum()
print('Ventas de los ultimos 3 meses : ', dataventas_totales[0])
print('======================================')
print('======================================')
meses = ['Febrero', 'Marzo', 'Abril']
gastos_totales = dataFrame.set_index('Mes').loc[meses].sum()
print('Gastos de los ultimos de Febrero a Abril : ',gastos_totales[1])
