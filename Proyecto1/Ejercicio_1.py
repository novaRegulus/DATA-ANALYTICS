# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
'''
variable que almacenara las ultimas 
ventas de los ultimos 5 días
'''

data_sales = pd.DataFrame(
        data = np.random.randint(0, 20,(6,5)),
        columns = ['PC', 'Teléfono', 'Impresora', 'Bocina', 'Joystic'],
        index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Precio Unitario']
    )

data_sales.loc['Precio Unitario'] = [15000, 6500, 1750, 320, 680]

transpuesta = data_sales.loc['Precio Unitario'].T



lunes = data_sales.loc["Lunes"].sum()
martes = data_sales.loc["Martes"].sum()
miercoles = data_sales.loc["Miercoles"].sum()
jueves = data_sales.loc["Jueves"].sum()
viernes = data_sales.loc["Viernes"].sum()
total_products = data_sales.loc["Precio Unitario"].sum() 
#obtengo el dato del total de ventas por porducto
data_sales['total_sales'] = [lunes, martes, miercoles, jueves, viernes, total_products]


monday    = transpuesta[0] * data_sales['total_sales'][0]
tuesday   = transpuesta[1] * data_sales['total_sales'][1]
wednesday = transpuesta[2] * data_sales['total_sales'][2]
thursday  = transpuesta[3] * data_sales['total_sales'][3]
friday    = transpuesta[4] * data_sales['total_sales'][4]



data_sales['total_sales'] = [monday, tuesday, wednesday, thursday, friday, total_products]


print("=========data_products=========")
print(data_sales)
print("=========5%=========")
print("***************************************")
print(data_sales)
data_sales['descuento'] = data_sales.total_sales * 0.005
print("***************************************")
data_sales['Total'] = (data_sales.total_sales) -  data_sales['descuento']
print(data_sales)

