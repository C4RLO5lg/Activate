# Carlos Ledezma García A00828114

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