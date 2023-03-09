#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:48:30 2023

@author: hiperion
"""

import pandas as pd

clientes_ingresos = {'Eliot': 25000, 'Darlene': 9780, 'Tyrell': 38000, 'Angela': 20000}

serie_ingresos = pd.Series(clientes_ingresos)

serie_final = pd.Series([serie_ingresos.min(), serie_ingresos.max(), serie_ingresos.mean()], index = ['Mínimo', 'Maximo', 'Media'])

print(serie_final)

