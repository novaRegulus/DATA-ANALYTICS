#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:48:30 2023

@author: hiperion
"""

import pandas as pd
'''
    Se importa la libreria pandas para trabajar con la información
'''

clientes_ingresos = {'Eliot': 25000, 'Darlene': 9780, 'Tyrell': 38000, 'Angela': 20000}
'''
    Se genera una varibale con los datos de clientes y sus ingresos mensuales
'''
serie_ingresos = pd.Series(clientes_ingresos)
'''
    se genera una serie con los ingresos de los clientes
'''
serie_final = pd.Series([serie_ingresos.min(), serie_ingresos.max(), serie_ingresos.mean()], index = ['Mínimo', 'Maximo', 'Media'])
'''
    Se genera una serie final con los estadisticos de los valores minimo, máximo y media en referencia a los ingresos de los clientes
'''
print(serie_final)

