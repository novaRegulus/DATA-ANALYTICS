#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:43:09 2023

@author: hiperion
"""


import pandas as pd
import numpy as np
'''
    Se importan las librerias numpy y pandas para el manejo de datos
'''
data = { 'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'], 'Ventas': [30500, 35600, 28300, 33900, 42500], 'Gastos': [22000, 23450, 18100, 35700, 32450] }
dataFrame = pd.DataFrame(data)
'''
    Se genera la data y el dataFrame con los valores por mes, ventas y Gastos
'''
print(dataFrame)
print('======================================')
print('======================================')
dataFrame['Columna 1'] = dataFrame.Gastos / dataFrame.Ventas * 100
'''
    Se agrega la Columna 1 obteniendo los gastos entre las ventas multiplicado por 100
'''
print(dataFrame)
print('======================================')
print('======================================')
dataFrame['Columna 2'] = np.where(dataFrame['Ventas'] >= 30000, 'Meta Superada', 'Meta no Superada')
'''
    Se agrega la Columna 2 opteniendo donde se agrega el texto *Meta Superada* solo si las Ventas fueron mayores o iguales
    a 30000, de lo contrario mostrara *Meta no Superada*
'''
print(dataFrame)
print('======================================')
print('======================================')
dataFrame['Columna 3'] = dataFrame.Gastos - dataFrame.Ventas
'''
    Se agrega la Columna 3 mostrando el sobregasto entre Gastos en relación a las ventas
'''
print(dataFrame)
print('======================================')
print('======================================')
meses = ['Marzo', 'Abril', 'Mayo']
dataventas_totales = dataFrame.set_index('Mes').loc[meses].sum()
'''
    Se genera una vairbale de ventas totales con el dataFrame con los ultimos 3 meses
    Finalmente se imprime mostrando el valor de las ventas totales de los meses referidos
'''
print('Ventas de los ultimos 3 meses : ', dataventas_totales[0])
print('======================================')
print('======================================')
meses = ['Febrero', 'Marzo', 'Abril']
gastos_totales = dataFrame.set_index('Mes').loc[meses].sum()
'''
    Se genera una vairbale de gastos totales con el dataFrame con los meses de Febrero a Abril
    Finalmente se imprime mostrando el valor de los gatsos totales de los meses referidos
'''
print('Gastos de los ultimos de Febrero a Abril : ',gastos_totales[1])
