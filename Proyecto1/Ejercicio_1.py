# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
'''
    Se importan las librerias numpy y pandas para el manejo de datos
'''

data_sales = pd.DataFrame(
        data = np.random.randint(0, 20,(6,5)),
        columns = ['PC', 'Teléfono', 'Impresora', 'Bocina', 'Joystic'],
        index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Precio Unitario']
    )
'''
    Se genera la variable data_sales, contiene el dataframe necesario para trabajar,
    la data consiste en número aleatorios para asimilar la cantida de productos vendidos,
    las columnas representan los productos
    los indices estan considerados como días y el ultimo indice representa el precio por producto
'''

data_sales.loc['Precio Unitario'] = [15000, 6500, 1750, 320, 680]
'''
    se agrega una columna con la el costo por producto
'''

transpuesta = data_sales.loc['Precio Unitario'].T
'''
    se genera una matriz transpuesta para los presios unitarios la cual servira para realizar operaciones
'''


lunes = data_sales.loc["Lunes"].sum()
martes = data_sales.loc["Martes"].sum()
miercoles = data_sales.loc["Miercoles"].sum()
jueves = data_sales.loc["Jueves"].sum()
viernes = data_sales.loc["Viernes"].sum()
total_products = data_sales.loc["Precio Unitario"].sum() 
#obtengo el dato del total de ventas por porducto
data_sales['total_sales'] = [lunes, martes, miercoles, jueves, viernes, total_products]
'''
    se obtiene la suma total por día de los productos
'''

monday    = transpuesta[0] * data_sales['total_sales'][0]
tuesday   = transpuesta[1] * data_sales['total_sales'][1]
wednesday = transpuesta[2] * data_sales['total_sales'][2]
thursday  = transpuesta[3] * data_sales['total_sales'][3]
friday    = transpuesta[4] * data_sales['total_sales'][4]
'''
    con ayuda de la matriz transpuesta se multiplica el total de proctos vendidos por el costo del precio por productos por día
'''


data_sales['total_sales'] = [monday, tuesday, wednesday, thursday, friday, total_products]
'''
    se asigana el valos a la columna *total_sales* con el total de ventas obtenidas del costo total por día
'''

print("=========data_products=========")
print(data_sales)
'''
    Se muestran los datos de los productos
'''
print("=========5%=========")
print("***************************************")
print(data_sales)
data_sales['descuento'] = data_sales.total_sales * 0.005
'''
    Se muestran los datos de los con el descuento del 5% por porducto
'''
print("***************************************")
data_sales['Total'] = (data_sales.total_sales) -  data_sales['descuento']
print(data_sales)
'''
    Se muestran el descuento real por procutos con el 5% 
'''
