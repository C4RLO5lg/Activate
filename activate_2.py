# Carlos Ledezma García A00828114
import pandas as pd
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

# Título y descripción
st.title('Dataset Walmart USA')
st.header('En esta página se muestra una base de datos de Walmart USA, la cual es filtrable por modo de envío (Ship Mode), categoría (Category) y por el descuento aplicado (Discount).')

#Sidebar
st.sidebar.title('Filtros de la base de datos')

# Radio
selected_smode = st.sidebar.radio("Select Ship Mode", data['Ship Mode'].unique())
st.write("Selected Ship Mode:", selected_smode)

# Selectbox
selected_category = st.sidebar.selectbox("Select Category", data['Category'].unique())
st.write(f"Selected Option: {selected_category!r}")

# Slider
optionals = st.sidebar.expander("Optional Configurations", True)
dis_select = optionals.slider("Select the Discount", min_value=float(data['Discount'].min()), max_value=float(data['Discount'].max()))
subset_dis = data[(data['Discount'] >= dis_select)]
st.write(f"Number of Records With this Discount {dis_select}:{subset_dis.shape[0]}")

data_fltr = data[(data['Ship Mode']==selected_smode)&
    (data['Category']==selected_category)&
    (data['Discount']==dis_select)
    ]

agree = st.sidebar.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(data_fltr)

# streamlit run activate_1.py