# Carlos Ledezma García A00828114

import pandas as pd
import streamlit as stgit 
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

# Gráfico de scatter
fig2, ax2 = plt.subplots()
ax2.scatter(data.Discount , data.Sales)
ax2.set_xlabel("Discount")
ax2.set_ylabel("Sales")
st.header("Grafica de Dispersión de cantidad de ventas por nivel de descuento")
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
ax3.hist(data.Discount)
st.header("Distribución de los descuentos por porcentaje (Representado decimalmente)")
st.pyplot(fig3)

# streamlit run activate_3.py