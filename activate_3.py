# Carlos Ledezma García A00828114
"""Descripción breve:
Desarrollar un código sobre la estructura de una aplicación web que
contenga 3 gráficas (barras, pastel y un histograma) sobre el proyecto de
visualización de analítica de datos para WalMart USA.
En el siguiente enlace podrás encontrar el enlace al conjunto de datos
que pertencen a WaltMart USA.
https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv

Instrucciones generales
El conjunto de datos de WalMart USA contiene los siguientes campos:
Row ID - Indice del registro de la orden
Order ID - Indice de la orden
Order Date - Fecha de la orden
Ship Date - Fecha de embarque
Ship Mode - Modo de embarque
Customer ID - Clave del cliente
Customer Name - Nombre del cliente
Segment - Segmento
Country - Pais
City - Ciudad
State - Estado
Postal Code - Código postal
Region - Region
Product ID - Clave del producto
Category - Categoría
Sub-Category - Sub categoría
Product Name - Nombre del producto
Sales - Ventas
Quantity - Cantidad vendida
Discount - Descuento aplicado
Profit - Ganancia

Ejercicio:
La estructura de la aplicación web deberá tener lo siguiente:
o Deberá incluir un titulo
o Deberá incluir un subtitulo (este puede ser opcional)
o Deberá incluir un breve párrafo que describa el objetivo de este proyecto de
analítica de datos; por ejemplo: predicción de ventas de productos de línea
blanca en el noroeste de los Estados Unidos.
o Una sección que contenga las gráficas antes mencionadas.
"""

import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

# Título y descripción
st.title('Dataset Walmart USA')
st.header('En esta página se muestra estdística descriptiva por medio de gráficos de una base de datos de Walmart USA.')

# Gráfico de barras
fig1, ax = plt.subplots()
ax.barh(data['Segment'], data['Sales'])
ax.set_title('Ventas por segmento')
st.pyplot(fig1)

# Gráfico de pastel
fig2 = px.pie(data,'Category', title = 'Proporción de ordenes por categoría')
st.write(fig2)

# Histograma
fig3 = px.histogram(data,'Discount', title = 'Distribución de los descuentos por porcentaje (Representado decimalmente)')
st.write(fig3)

# streamlit run activate_3.py