# Carlos Ledezma García A00828114

import pandas as pd
import streamlit as st

url ='https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

st.title('Dataset Uber')
st.header('En esta página se muestra un mapa de viajes de Uber en Nueva York, filtrable por hora del día')

@st.cache
def load_data(nrows):
    data = pd.read_csv(url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data

data = load_data(20000)

hours = st.sidebar.expander("Hora del viaje", True)
hours_select = hours.slider("Seleccione la hora del día", min_value= 0, max_value= 23)

filtered_data = data[data['date/time'].dt.hour == hours_select]

st.map(filtered_data)